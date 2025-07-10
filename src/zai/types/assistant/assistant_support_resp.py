from typing import List

from ...core import BaseModel

__all__ = ['AssistantSupportResp']


class AssistantSupport(BaseModel):
	"""
	Assistant support information

	Attributes:
		assistant_id (str): Assistant identifier for conversation
		created_at (int): Assistant creation timestamp
		updated_at (int): Last update timestamp
		name (str): Assistant display name
		avatar (str): Assistant avatar URL or identifier
		description (str): Assistant description text
		status (str): Assistant status (currently only 'publish')
		tools (List[str]): List of tool names supported by the assistant
		starter_prompts (List[str]): Recommended startup prompts for the assistant
	"""
	assistant_id: str
	created_at: int
	updated_at: int
	name: str
	avatar: str
	description: str
	status: str
	tools: List[str]
	starter_prompts: List[str]


class AssistantSupportResp(BaseModel):
	"""
	Response for assistant support query

	Attributes:
		code (int): Response status code
		msg (str): Response message
		data (List[AssistantSupport]): List of available assistants
	"""
	code: int
	msg: str
	data: List[AssistantSupport]
