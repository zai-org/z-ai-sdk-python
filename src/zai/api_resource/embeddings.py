from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

import httpx

from ..core import NOT_GIVEN, BaseAPI, Body, Headers, NotGiven, make_request_options
from ..types.embeddings import EmbeddingsResponded

if TYPE_CHECKING:
	from .._client import ZaiClient


class Embeddings(BaseAPI):
	"""
	Embeddings API resource

	Attributes:
		client (ZaiClient): The ZAI client instance
	"""
	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def create(
		self,
		*,
		input: Union[str, List[str], List[int], List[List[int]]],
		model: Union[str],
		dimensions: Union[int] | NotGiven = NOT_GIVEN,
		encoding_format: str | NotGiven = NOT_GIVEN,
		user: str | NotGiven = NOT_GIVEN,
		request_id: Optional[str] | NotGiven = NOT_GIVEN,
		sensitive_word_check: Optional[object] | NotGiven = NOT_GIVEN,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		disable_strict_validation: Optional[bool] | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> EmbeddingsResponded:
		"""
		Create embeddings for the given input

		Arguments:
			input (Union[str, List[str], List[int], List[List[int]]]): Input text or tokens to embed
			model (str): Model name to use for embedding generation
			dimensions (Union[int]): Number of dimensions for the embedding vectors
			encoding_format (str): Format for encoding the embeddings
			user (str): User identifier
			request_id (Optional[str]): Request identifier
			sensitive_word_check (Optional[object]): Sensitive word checking configuration
			extra_headers (Headers): Additional HTTP headers
			extra_body (Body): Additional request body parameters
			disable_strict_validation (Optional[bool]): Whether to disable strict validation
			timeout (float | httpx.Timeout): Request timeout
		"""
		_cast_type = EmbeddingsResponded
		if disable_strict_validation:
			_cast_type = object
		return self._post(
			'/embeddings',
			body={
				'input': input,
				'model': model,
				'dimensions': dimensions,
				'encoding_format': encoding_format,
				'user': user,
				'request_id': request_id,
				'sensitive_word_check': sensitive_word_check,
			},
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=_cast_type,
			stream=False,
		)
