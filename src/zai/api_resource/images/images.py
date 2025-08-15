from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from zai.core import NOT_GIVEN, BaseAPI, Body, Headers, NotGiven, make_request_options
from zai.types.image import ImagesResponded
from zai.types.sensitive_word_check import SensitiveWordCheckRequest

if TYPE_CHECKING:
	from zai._client import ZaiClient


class Images(BaseAPI):
	"""
	API resource for image generation operations
	"""

	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def generations(
		self,
		*,
		prompt: str,
		model: str | NotGiven = NOT_GIVEN,
		n: Optional[int] | NotGiven = NOT_GIVEN,
		quality: Optional[str] | NotGiven = NOT_GIVEN,
		response_format: Optional[str] | NotGiven = NOT_GIVEN,
		size: Optional[str] | NotGiven = NOT_GIVEN,
		style: Optional[str] | NotGiven = NOT_GIVEN,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		user: str | NotGiven = NOT_GIVEN,
		request_id: Optional[str] | NotGiven = NOT_GIVEN,
		user_id: Optional[str] | NotGiven = NOT_GIVEN,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		disable_strict_validation: Optional[bool] | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
		watermark_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
	) -> ImagesResponded:
		"""
		Generate images from text prompts

		Arguments:
			prompt (str): Text description of the desired image
			model (str): The model to use for image generation
			n (Optional[int]): Number of images to generate
			quality (Optional[str]): Quality level of the generated images
			response_format (Optional[str]): Format of the response
			size (Optional[str]): Size of the generated images
			style (Optional[str]): Style of the generated images
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
			user (str): User identifier
			request_id (Optional[str]): Unique identifier for the request
			user_id (Optional[str]): User identifier
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			disable_strict_validation (Optional[bool]): Whether to disable strict validation
			timeout (float | httpx.Timeout): Request timeout
			watermark_enabled (Optional[bool]): Whether to enable watermark on generated images
		"""
		_cast_type = ImagesResponded
		if disable_strict_validation:
			_cast_type = object
		return self._post(
			'/images/generations',
			body={
				'prompt': prompt,
				'model': model,
				'n': n,
				'quality': quality,
				'response_format': response_format,
				'sensitive_word_check': sensitive_word_check,
				'size': size,
				'style': style,
				'user': user,
				'user_id': user_id,
				'request_id': request_id,
				'watermark_enabled': watermark_enabled,
			},
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=_cast_type,
			stream=False,
		)
