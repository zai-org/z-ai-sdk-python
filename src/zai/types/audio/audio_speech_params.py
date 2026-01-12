from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

from zai.types.sensitive_word_check import SensitiveWordCheckRequest


class AudioSpeechParams(TypedDict, total=False):
	"""
	Parameters for audio speech generation

	Attributes:
		model (str): Model encoding
		input (str): Text to be converted to speech
		voice (str): Voice tone for speech generation
		response_format (str): Format of the generated audio file
		watermark_enabled (Optional[bool]): Whether to enable watermark on generated audio
		encode_format (str): Encoding format for streaming response (base64 or hex)
		speed (float): Speech speed, default 1.0, range [0.5, 2]
		volume (float): Audio volume, default 1.0, range (0, 10]
		stream (bool): Whether to use streaming output
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
		request_id (str): Request ID passed by client, must be unique; used to distinguish each request,
			platform will generate default if not provided by client
		user_id (str): User ID
	"""

	model: str
	input: str
	voice: str
	response_format: str
	watermark_enabled: Optional[bool]
	encode_format: str
	speed: float
	volume: float
	stream: bool
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
