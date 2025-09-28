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
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
		request_id (str): Request ID passed by client, must be unique; used to distinguish each request,
			platform will generate default if not provided by client
		user_id (str): User ID
	"""

	model: str
	input: str
	voice: str
	response_format: str
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
	encode_format: str
	speed: float
	volume: float
	stream: bool
