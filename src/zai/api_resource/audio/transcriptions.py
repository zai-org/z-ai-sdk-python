from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Mapping, Optional, cast

import httpx
from typing_extensions import Literal

from zai.core._utils import extract_files

from ...core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	FileTypes,
	Headers,
	NotGiven,
	StreamResponse,
	deepcopy_minimal,
	make_request_options,
	maybe_transform,
)
from ...types.audio import transcriptions_create_param
from ...types.chat.chat_completion import Completion
from ...types.chat.chat_completion_chunk import ChatCompletionChunk
from ...types.sensitive_word_check import SensitiveWordCheckRequest

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
	from ..._client import ZaiClient


__all__ = ['Transcriptions']


class Transcriptions(BaseAPI):
	"""
	API resource for audio transcription operations
	"""
	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def create(
		self,
		*,
		file: FileTypes,
		model: str,
		request_id: Optional[str] | NotGiven = NOT_GIVEN,
		user_id: Optional[str] | NotGiven = NOT_GIVEN,
		stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
		temperature: Optional[float] | NotGiven = NOT_GIVEN,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> Completion | StreamResponse[ChatCompletionChunk]:
		"""
		Transcribe audio files to text
		
		Arguments:
			file (FileTypes): Audio file to transcribe
			model (str): The model to use for transcription
			request_id (Optional[str]): Unique identifier for the request
			user_id (Optional[str]): User identifier
			stream (Optional[Literal[False]] | Literal[True]): Whether to stream the response
			temperature (Optional[float]): Sampling temperature for transcription
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		if temperature is not None and temperature != NOT_GIVEN:
			if temperature <= 0:
				temperature = 0.01
			if temperature >= 1:
				temperature = 0.99

		body = deepcopy_minimal(
			{
				'model': model,
				'file': file,
				'request_id': request_id,
				'user_id': user_id,
				'temperature': temperature,
				'sensitive_word_check': sensitive_word_check,
				'stream': stream,
			}
		)
		files = extract_files(cast(Mapping[str, object], body), paths=[['file']])
		if files:
			extra_headers = {
				'Content-Type': 'multipart/form-data',
				**(extra_headers or {}),
			}
		return self._post(
			'/audio/transcriptions',
			body=maybe_transform(body, transcriptions_create_param.TranscriptionsParam),
			files=files,
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=Completion,
			stream=stream or False,
			stream_cls=StreamResponse[ChatCompletionChunk],
		)
