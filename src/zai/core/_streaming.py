# -*- coding:utf-8 -*-
from __future__ import annotations

import inspect
import json
from typing import TYPE_CHECKING, Any, Generic, Iterator, Mapping, Type, cast

import httpx
from typing_extensions import TypeGuard

from . import get_origin
from ._base_type import ResponseT
from ._errors import APIResponseError
from ._utils import extract_type_var_from_base, is_mapping

_FIELD_SEPARATOR = ':'

if TYPE_CHECKING:
	from ._http_client import HttpClient


class StreamResponse(Generic[ResponseT]):
	"""
	Stream response class, used to stream response from server.

	Attributes:
		response: The response from server.
		_cast_type: The type of response.
	"""

	response: httpx.Response
	_cast_type: Type[ResponseT]

	def __init__(
		self,
		*,
		cast_type: Type[ResponseT],
		response: httpx.Response,
		client: HttpClient,
	) -> None:
		self.response = response
		self._cast_type = cast_type
		self._data_process_func = client._process_response_data
		self._stream_chunks = self.__stream__()

	def __next__(self) -> ResponseT:
		return self._stream_chunks.__next__()

	def __iter__(self) -> Iterator[ResponseT]:
		for item in self._stream_chunks:
			yield item

	def __stream__(self) -> Iterator[ResponseT]:
		sse_line_parser = SSELineParser()
		iterator = sse_line_parser.iter_lines(self.response.iter_lines())

		for sse in iterator:
			if sse.data.startswith('[DONE]'):
				break
			if sse.event is None:
				data = sse.json_data()
				if isinstance(data, Mapping) and data.get('agent_id'):
					yield self._data_process_func(
						data=data,
						cast_type=self._cast_type,
						response=self.response,
					)
					continue
				if isinstance(data, Mapping) and data.get('error'):
					raise APIResponseError(
						message='An error occurred during streaming',
						request=self.response.request,
						json_data=data['error'],
					)
			if sse.event is None:
				data = sse.json_data()
				if is_mapping(data) and data.get('error'):
					message = None
					error = data.get('error')
					if is_mapping(error):
						message = error.get('message')
					if not message or not isinstance(message, str):
						message = 'An error occurred during streaming'

					raise APIResponseError(
						message=message,
						request=self.response.request,
						json_data=data['error'],
					)
				yield self._data_process_func(data=data, cast_type=self._cast_type, response=self.response)

			else:
				data = sse.json_data()

				if sse.event == 'error' and is_mapping(data) and data.get('error'):
					message = None
					error = data.get('error')
					if is_mapping(error):
						message = error.get('message')
					if not message or not isinstance(message, str):
						message = 'An error occurred during streaming'

					raise APIResponseError(
						message=message,
						request=self.response.request,
						json_data=data['error'],
					)
				yield self._data_process_func(data=data, cast_type=self._cast_type, response=self.response)

		for sse in iterator:
			pass

class AsyncStreamResponse(Generic[ResponseT]):
    """Provides the core interface to iterate over an asynchronous stream response."""

    response: httpx.Response
    _cast_type: Type[ResponseT]

    def __init__(
        self,
        *,
        cast_to: type[ResponseT],
        response: httpx.Response,
        client: HttpClient,
    ) -> None:
        self.response = response
        self._cast_to = cast_to
        self._client = client
        self._decoder = client._make_sse_decoder()
        self._iterator = self.__stream__()

    async def __anext__(self) -> ResponseT:
        return await self._iterator.__anext__()

    async def __aiter__(self) -> AsyncIterator[ResponseT]:
        async for item in self._iterator:
            yield item

    async def _iter_events(self) -> AsyncIterator[Event]:
        async for sse in self._decoder.aiter_bytes(self.response.aiter_bytes()):
            yield sse

    async def __stream__(self) -> AsyncIterator[ResponseT]:
        cast_to = cast(Any, self._cast_to)
        response = self.response
        process_data = self._client._process_response_data
        iterator = self._iter_events()

        async for sse in iterator:
            if sse.data.startswith("[DONE]"):
                break

            # we have to special case the Assistants `thread.` events since we won't have an "event" key in the data
            if sse.event and sse.event.startswith("thread."):
                data = sse.json()

                if sse.event == "error" and is_mapping(data) and data.get("error"):
                    message = None
                    error = data.get("error")
                    if is_mapping(error):
                        message = error.get("message")
                    if not message or not isinstance(message, str):
                        message = "An error occurred during streaming"

                    raise APIError(
                        message=message,
                        request=self.response.request,
                        body=data["error"],
                    )

                yield process_data(data={"data": data, "event": sse.event}, cast_to=cast_to, response=response)
            else:
                data = sse.json()
                if is_mapping(data) and data.get("error"):
                    message = None
                    error = data.get("error")
                    if is_mapping(error):
                        message = error.get("message")
                    if not message or not isinstance(message, str):
                        message = "An error occurred during streaming"

                    raise APIError(
                        message=message,
                        request=self.response.request,
                        body=data["error"],
                    )

                yield process_data(data=data, cast_to=cast_to, response=response)

        # Ensure the entire stream is consumed
        async for _sse in iterator:
            ...

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        """
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        """
        await self.response.aclose()

class Event(object):
	def __init__(
		self,
		event: str | None = None,
		data: str | None = None,
		id: str | None = None,
		retry: int | None = None,
	):
		self._event = event
		self._data = data
		self._id = id
		self._retry = retry

	def __repr__(self):
		data_len = len(self._data) if self._data else 0
		return (
			f'Event(event={self._event}, data={self._data} ,data_length={data_len}, id={self._id}, retry={self._retry})'
		)

	@property
	def event(self):
		return self._event

	@property
	def data(self):
		return self._data

	def json_data(self):
		return json.loads(self._data)

	@property
	def id(self):
		return self._id

	@property
	def retry(self):
		return self._retry


class SSELineParser:
	_data: list[str]
	_event: str | None
	_retry: int | None
	_id: str | None

	def __init__(self):
		self._event = None
		self._data = []
		self._id = None
		self._retry = None

	def iter_lines(self, lines: Iterator[str]) -> Iterator[Event]:
		for line in lines:
			line = line.rstrip('\n')
			if not line:
				if self._event is None and not self._data and self._id is None and self._retry is None:
					continue
				sse_event = Event(
					event=self._event,
					data='\n'.join(self._data),
					id=self._id,
					retry=self._retry,
				)
				self._event = None
				self._data = []
				self._id = None
				self._retry = None

				yield sse_event
			self.decode_line(line)

	def decode_line(self, line: str):
		if line.startswith(':') or not line:
			return

		field, _p, value = line.partition(':')

		if value.startswith(' '):
			value = value[1:]
		if field == 'data':
			self._data.append(value)
		elif field == 'event':
			self._event = value
		elif field == 'retry':
			try:
				self._retry = int(value)
			except (TypeError, ValueError):
				pass
		return


def is_stream_class_type(typ: type) -> TypeGuard[type[StreamResponse[object]]]:
	"""TypeGuard for determining whether or not the given type is a subclass of `Stream` / `AsyncStream`"""
	origin = get_origin(typ) or typ
	return inspect.isclass(origin) and issubclass(origin, StreamResponse)


def extract_stream_chunk_type(
	stream_cls: type,
	*,
	failure_message: str | None = None,
) -> type:
	"""Given a type like `StreamResponse[T]`, returns the generic type variable `T`.

	This also handles the case where a concrete subclass is given, e.g.
	```py
	class MyStream(StreamResponse[bytes]):
	    ...

	extract_stream_chunk_type(MyStream) -> bytes
	```
	"""

	return extract_type_var_from_base(
		stream_cls,
		index=0,
		generic_bases=cast('tuple[type, ...]', (StreamResponse,)),
		failure_message=failure_message,
	)
