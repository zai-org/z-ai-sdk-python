from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

from zai.types.sensitive_word_check import SensitiveWordCheckRequest


class TranscriptionsParam(TypedDict, total=False):
	"""
	Parameters for creating a transcription.

	Attributes:
		model (str): Model encoding.
		file (str): Audio file to transcribe.
		file_base64 (str): Base64 encoded audio file (alternative to file).
		prompt (str): Previous transcription result for context in long text scenarios.
		hotwords (List[str]): Hot words to improve recognition rate for specific domain vocabulary.
		stream (bool): Whether to use streaming output.
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration.
		request_id (str): Passed by the client, must ensure uniqueness; used to distinguish
			the unique identifier of each request. If not provided by the client,
			the platform will generate it by default.
		user_id (str): Client user ID.
	"""

	model: str
	file: str
	file_base64: str
	prompt: str
	hotwords: List[str]
	stream: bool
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
