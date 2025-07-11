from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ['VideoCreateParams']

from ..sensitive_word_check import SensitiveWordCheckRequest


class VideoCreateParams(TypedDict, total=False):
	"""
	Parameters for video creation

	Attributes:
		model (str): Model encoding
		prompt (str): Text description of the desired video
		image_url (str): Image URL for image-to-video generation (supports URL or Base64 format)
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
		request_id (str): Request ID passed by client, must be unique; used to distinguish each request,
			platform will generate default if not provided by client
		user_id (str): User ID
	"""
	model: str
	prompt: str
	image_url: str
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
