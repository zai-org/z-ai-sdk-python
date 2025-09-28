from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict


class VoiceListParams(TypedDict, total=False):
	"""
	Parameters for listing voices
	
	Attributes:
		voice_type (Optional[str]): Type of voice to filter by
		voice_name (Optional[str]): Name of voice to filter by
		request_id (Optional[str]): Optional request ID for tracking
	"""
	
	voice_type: Optional[str]
	voice_name: Optional[str]
	request_id: Optional[str]