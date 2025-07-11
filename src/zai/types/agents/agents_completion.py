from typing import List, Optional

from ...core import BaseModel

__all__ = ['AgentsCompletion', 'AgentsCompletionUsage']


class AgentsCompletionMessage(BaseModel):
	"""
	Represents a message in an agents completion response.

	Attributes:
		content (Optional[object]): The content of the message
		role (str): The role of the message sender
	"""

	content: Optional[object] = None
	role: str


class AgentsCompletionUsage(BaseModel):
	"""
	Represents token usage statistics for agents completion.

	Attributes:
		prompt_tokens (int): Number of tokens in the prompt
		completion_tokens (int): Number of tokens in the completion
		total_tokens (int): Total number of tokens used
	"""

	prompt_tokens: int
	completion_tokens: int
	total_tokens: int


class AgentsCompletionChoice(BaseModel):
	"""
	Represents a choice in the agents completion response.

	Attributes:
		index (int): Index of this choice
		finish_reason (str): Reason why the generation finished
		message (AgentsCompletionMessage): The completion message
	"""

	index: int
	finish_reason: str
	message: AgentsCompletionMessage


class AgentsError:
	"""
	Represents an error in agents completion.

	Attributes:
		code (Optional[str]): Error code
		message (Optional[str]): Error message
	"""

	code: Optional[str] = None
	message: Optional[str] = None


class AgentsCompletion(BaseModel):
	"""
	Represents a completion response from an agent.

	Attributes:
		agent_id (Optional[str]): Unique identifier of the agent
		conversation_id (Optional[str]): Unique identifier of the conversation
		status (Optional[str]): Status of the completion
		choices (List[AgentsCompletionChoice]): List of completion choices
		request_id (Optional[str]): Unique identifier of the request
		id (Optional[str]): Unique identifier of the completion
		usage (Optional[AgentsCompletionUsage]): Token usage statistics
		error (Optional[AgentsError]): Error information if any
	"""

	agent_id: Optional[str] = None
	conversation_id: Optional[str] = None
	status: Optional[str] = None
	choices: List[AgentsCompletionChoice]
	request_id: Optional[str] = None
	id: Optional[str] = None
	usage: Optional[AgentsCompletionUsage] = None
	error: Optional[AgentsError] = None
