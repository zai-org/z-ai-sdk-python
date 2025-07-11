from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ['TranscriptionsParam']

from ..sensitive_word_check import SensitiveWordCheckRequest


class TranscriptionsParam(TypedDict, total=False):
	"""
	Parameters for creating a transcription.

	Attributes:
		model (str): Model encoding.
		temperature (float): Sampling temperature.
		stream (bool): Whether to use streaming output.
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration.
		request_id (str): Passed by the client, must ensure uniqueness; used to distinguish
			the unique identifier of each request. If not provided by the client,
			the platform will generate it by default.
		user_id (str): Client user ID.
	"""

	model: str
	temperature: float
	stream: bool
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
	request_id: str
	user_id: str
