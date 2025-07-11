from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List, Optional, Union

import httpx
from typing_extensions import Literal

from ...core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	Headers,
	NotGiven,
	StreamResponse,
	deepcopy_minimal,
	make_request_options,
	maybe_transform,
)
from ...types.tools import WebSearch, WebSearchChunk, tools_web_search_params

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
	from ..._client import ZaiClient

__all__ = ['Tools']


class Tools(BaseAPI):
	"""
	API resource for tools functionality.

	Provides access to various tool operations including web search.
	"""
	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def web_search(
		self,
		*,
		model: str,
		request_id: Optional[str] | NotGiven = NOT_GIVEN,
		stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
		messages: Union[str, List[str], List[int], object, None],
		scope: Optional[str] | NotGiven = NOT_GIVEN,
		location: Optional[str] | NotGiven = NOT_GIVEN,
		recent_days: Optional[int] | NotGiven = NOT_GIVEN,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> WebSearch | StreamResponse[WebSearchChunk]:
		"""
		Perform web search using AI models
		
		Arguments:
			model (str): The model to use for web search
			request_id (Optional[str]): Unique identifier for the request
			stream (Optional[Literal[False]] | Literal[True]): Whether to stream the response
			messages (Union[str, List[str], List[int], object, None]): Search query or messages
			scope (Optional[str]): Search scope or domain
			location (Optional[str]): Geographic location for search
			recent_days (Optional[int]): Number of recent days to search within
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		body = deepcopy_minimal(
			{
				'model': model,
				'request_id': request_id,
				'messages': messages,
				'stream': stream,
				'scope': scope,
				'location': location,
				'recent_days': recent_days,
			}
		)
		return self._post(
			'/tools',
			body=maybe_transform(body, tools_web_search_params.WebSearchParams),
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=WebSearch,
			stream=stream or False,
			stream_cls=StreamResponse[WebSearchChunk],
		)
