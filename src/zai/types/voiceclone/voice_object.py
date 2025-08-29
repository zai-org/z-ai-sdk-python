from typing import List

from zai.core import BaseModel


class VoiceCloneResult(BaseModel):
	"""
	Voice cloning result
	
	Attributes:
		voice (str): Voice
		file_id (str): Audio preview file ID
		file_purpose (str): File purpose
	"""
	
	voice: str
	file_id: str
	file_purpose: str


class VoiceDeleteResult(BaseModel):
	"""
	Voice deletion result
	
	Attributes:
		voice (str): Voice
		update_time (str): Delete time (format: yyyy-MM-dd HH:mm:ss)
	"""
	
	voice: str
	update_time: str


class VoiceData(BaseModel):
	"""
	Voice data information
	
	Attributes:
		voice (str): Voice
		voice_name (str): Voice name
		voice_type (str): Voice type
		download_url (str): Download URL
		create_time (str): Create time (format: yyyy-MM-dd HH:mm:ss)
	"""
	
	voice: str
	voice_name: str
	voice_type: str
	download_url: str
	create_time: str


class VoiceListResult(BaseModel):
	"""
	Voice list result
	
	Attributes:
		voice_list (List[VoiceData]): List of voices
	"""
	
	voice_list: List[VoiceData]