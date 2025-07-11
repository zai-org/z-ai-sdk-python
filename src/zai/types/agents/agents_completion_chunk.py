from typing import List, Optional

from ...core import BaseModel

__all__ = [
	'AgentsCompletionUsage',
	'AgentsCompletionChunk',
	'AgentsChoice',
	'AgentsChoiceDelta',
]


class AgentsChoiceDelta(BaseModel):
	"""
	Represents the delta changes in an agents streaming choice.

	Attributes:
		content (Optional[object]): The content delta
		role (Optional[str]): The role of the message sender
	"""
	content: Optional[object] = None
	role: Optional[str] = None


class AgentsChoice(BaseModel):
	"""
	Represents a choice in the agents streaming response.

	Attributes:
		delta (AgentsChoiceDelta): The delta changes for this choice
		finish_reason (Optional[str]): Reason why the generation finished
		index (int): Index of this choice in the response
	"""
	delta: AgentsChoiceDelta
	finish_reason: Optional[str] = None
	index: int


class AgentsCompletionUsage(BaseModel):
	"""
	Represents token usage statistics for agents completion chunk.

	Attributes:
		prompt_tokens (int): Number of tokens in the prompt
		completion_tokens (int): Number of tokens in the completion
		total_tokens (int): Total number of tokens used
	"""
	prompt_tokens: int
	completion_tokens: int
	total_tokens: int


class AgentsError:
	"""
	Represents an error in agents completion chunk.

	Attributes:
		code (Optional[str]): Error code
		message (Optional[str]): Error message
	"""
	code: Optional[str] = None
	message: Optional[str] = None


class AgentsCompletionChunk(BaseModel):
	"""
	Represents a chunk in the agents streaming completion response.

	Attributes:
		agent_id (Optional[str]): Unique identifier of the agent
		conversation_id (Optional[str]): Unique identifier of the conversation
		id (Optional[str]): Unique identifier of the chunk
		choices (List[AgentsChoice]): List of choices in this chunk
		usage (Optional[AgentsCompletionUsage]): Token usage statistics
		error (Optional[AgentsError]): Error information if any
	"""
	agent_id: Optional[str] = None
	conversation_id: Optional[str] = None
	id: Optional[str] = None
	choices: List[AgentsChoice]
	usage: Optional[AgentsCompletionUsage] = None
	error: Optional[AgentsError] = None
