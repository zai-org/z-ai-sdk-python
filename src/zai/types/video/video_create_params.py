from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

from zai.types.sensitive_word_check import SensitiveWordCheckRequest


class VideoCreateParams(TypedDict, total=False):
	"""
	Parameters for video creation

	Attributes:
		model (str): Model encoding
		prompt (str): Text description of the desired video
		image_url (str | list | dict): Image URL(s) or object for image-to-video generation (supports URL, Base64, or object)
		quality (str): Output mode, "quality" or "speed"
		with_audio (bool): Whether to include audio in the video
		size (str): Size/resolution of the generated video
		duration (int): Duration of the video in seconds
		fps (int): Frames per second for the video
		style (str): Style, e.g., "general", "anime"
		aspect_ratio (str): Aspect ratio, e.g., "16:9", "9:16", "1:1"
		movement_amplitude (str): Movement amplitude, e.g., "auto", "small", "medium", "large"
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
		request_id (str): Request ID passed by client, must be unique; used to distinguish each request,
			platform will generate default if not provided by client
		user_id (str): User ID
	"""
	model: str
	prompt: str
	image_url: str | list[str] | dict
	quality: str
	with_audio: bool
	size: str
	duration: int
	fps: int
	style: str
	aspect_ratio: str
	movement_amplitude: str
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
