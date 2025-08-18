from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

import httpx

from zai.core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	Headers,
	NotGiven,
	deepcopy_minimal,
	make_request_options,
	maybe_transform,
)
from zai.types.sensitive_word_check import SensitiveWordCheckRequest
from zai.types.video import VideoObject, video_create_params

if TYPE_CHECKING:
	from zai._client import ZaiClient


class Videos(BaseAPI):
	"""
	API resource for video generation operations
	"""

	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def generations(
		self,
		*,
		model: str,
		prompt: str = None,
		image_url: str | List[str] | dict | None = None,
		quality: str = None,
		with_audio: bool = None,
		size: str = None,
		duration: int = None,
		fps: int = None,
		style: str = None,
		aspect_ratio: str = None,
		movement_amplitude: str = None,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		request_id: str = None,
		user_id: str = None,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
		watermark_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
	) -> VideoObject:
		"""
		Generate videos from text prompts or images

		Arguments:
			model (str): The model to use for video generation
			prompt (str): Text description for video generation
			image_url (str | List[str] | dict): Image(s) for video generation (URL, Base64, or object)
			quality (str): Output mode, "quality" or "speed"
			with_audio (bool): Whether to include audio in the video
			size (str): Size/resolution of the generated video
			duration (int): Duration of the video in seconds
			fps (int): Frames per second for the video
			style (str): Style, e.g., "general", "anime"
			aspect_ratio (str): Aspect ratio, e.g., "16:9", "9:16", "1:1"
			movement_amplitude (str): Movement amplitude, e.g., "auto", "small", "medium", "large"
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
			request_id (str): Unique identifier for the request
			user_id (str): User identifier
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
			watermark_enabled (Optional[bool]): Whether to enable watermark on generated videos
		"""
		if not model:
			raise ValueError('`model` must be provided.')
		body = deepcopy_minimal(
			{
				'model': model,
				'prompt': prompt,
				'image_url': image_url,
				'quality': quality,
				'with_audio': with_audio,
				'size': size,
				'duration': duration,
				'fps': fps,
				'style': style,
				'aspect_ratio': aspect_ratio,
				'movement_amplitude': movement_amplitude,
				'sensitive_word_check': sensitive_word_check,
				'request_id': request_id,
				'user_id': user_id,
				'watermark_enabled': watermark_enabled,
			}
		)
		return self._post(
			'/videos/generations',
			body=maybe_transform(body, video_create_params.VideoCreateParams),
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=VideoObject,
		)

	def retrieve_videos_result(
		self,
		id: str,
		*,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> VideoObject:
		"""
		Retrieve the result of a video generation operation

		Arguments:
			id (str): Unique identifier for the video generation operation
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		if not id:
			raise ValueError('At least one of `id` must be provided.')

		return self._get(
			f'/async-result/{id}',
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=VideoObject,
		)
