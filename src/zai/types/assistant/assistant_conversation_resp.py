from typing import List

from ...core import BaseModel

__all__ = ['ConversationUsageListResp']


class Usage(BaseModel):
	"""
	Token usage statistics

	Attributes:
		prompt_tokens (int): Number of tokens in user input
		completion_tokens (int): Number of tokens in model output
		total_tokens (int): Total number of tokens used
	"""
	prompt_tokens: int
	completion_tokens: int
	total_tokens: int


class ConversationUsage(BaseModel):
	"""
	Conversation usage information

	Attributes:
		id (str): Unique conversation identifier
		assistant_id (str): Assistant identifier
		create_time (int): Conversation creation timestamp
		update_time (int): Last update timestamp
		usage (Usage): Token usage statistics for this conversation
	"""
	id: str
	assistant_id: str
	create_time: int
	update_time: int
	usage: Usage


class ConversationUsageList(BaseModel):
	"""
	List of conversation usage data

	Attributes:
		assistant_id (str): Assistant identifier
		has_more (bool): Whether there are more pages available
		conversation_list (List[ConversationUsage]): List of conversation usage records
	"""
	assistant_id: str
	has_more: bool
	conversation_list: List[ConversationUsage]


class ConversationUsageListResp(BaseModel):
	"""
	Response for conversation usage list query

	Attributes:
		code (int): Response status code
		msg (str): Response message
		data (ConversationUsageList): Conversation usage data
	"""
	code: int
	msg: str
	data: ConversationUsageList
