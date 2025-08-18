from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict


class VoiceDeleteParams(TypedDict, total=False):
	"""
	Parameters for voice deletion
	
	Attributes:
		voice_id (str): The ID of the voice to delete
		request_id (Optional[str]): Optional request ID for tracking
	"""
	
	voice_id: Required[str]
	request_id: Optional[str]