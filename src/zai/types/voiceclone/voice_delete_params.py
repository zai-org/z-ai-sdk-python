from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict


class VoiceDeleteParams(TypedDict, total=False):
	"""
	Parameters for voice deletion
	
	Attributes:
		voice (str): The voice to delete
		request_id (Optional[str]): Optional request ID for tracking
	"""
	
	voice: Required[str]
	request_id: Optional[str]