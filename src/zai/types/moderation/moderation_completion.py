from typing import Dict, List, Optional, Union

from zai.core import BaseModel


class Completion(BaseModel):
	"""
	Moderation completion response
	
	Attributes:
		model: The model used for moderation
		input: The input content for moderation (can be string, list of strings, or dictionary)
	"""
	model: Optional[str] = None
	input: Optional[Union[str, List[str], Dict]] = None
