from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict


class VoiceCloneParams(TypedDict, total=False):
	"""
	Parameters for voice cloning
	
	Attributes:
		voice_name (str): Name for the cloned voice
		voice_text_input (str): Text content corresponding to the sample audio
		voice_text_output (str): Target text for preview audio
		file_id (str): File ID of the uploaded audio file
		request_id (Optional[str]): Optional request ID for tracking
	"""
	
	voice_name: Required[str]
	voice_text_input: Required[str]
	voice_text_output: Required[str]
	file_id: Required[str]
	request_id: Optional[str]