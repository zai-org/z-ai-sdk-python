from typing import Any, Dict, List, Optional

from ...core import BaseModel
from .message import MessageContent

__all__ = ['AssistantCompletion', 'CompletionUsage']


class ErrorInfo(BaseModel):
	"""
	Error information for assistant operations

	Attributes:
		code (str): Error code identifier
		message (str): Human-readable error message
	"""

	code: str
	message: str


class AssistantChoice(BaseModel):
	"""
	Assistant response choice information

	Attributes:
		index (int): Choice result index
		delta (MessageContent): Current conversation output message content
		finish_reason (str): Inference end reason (
			stop: natural end or stop words;
			sensitive: content intercepted by security audit;
			network_error: service exception)
		metadata (dict): Metadata extension field
	"""

	index: int
	delta: MessageContent
	finish_reason: str
	metadata: dict


class CompletionUsage(BaseModel):
	"""
	Token usage statistics for completion

	Attributes:
		prompt_tokens (int): Number of input tokens
		completion_tokens (int): Number of output tokens
		total_tokens (int): Total number of tokens used
	"""

	prompt_tokens: int
	completion_tokens: int
	total_tokens: int


class AssistantCompletion(BaseModel):
	"""
	Assistant completion response

	Attributes:
		id (str): Unique request identifier
		conversation_id (str): Conversation identifier
		assistant_id (str): Assistant identifier
		created (int): Request creation time as Unix timestamp
		status (str): Response status (completed: generation finished,
                      in_progress: generating, failed: generation exception)
		last_error (Optional[ErrorInfo]): Error information if generation failed
		choices (List[AssistantChoice]): List of response choices with incremental information
		metadata (Optional[Dict[str, Any]]): Optional metadata extension field
		usage (Optional[CompletionUsage]): Token usage statistics
	"""

	id: str
	conversation_id: str
	assistant_id: str
	created: int
	status: str
	last_error: Optional[ErrorInfo]
	choices: List[AssistantChoice]
	metadata: Optional[Dict[str, Any]]
	usage: Optional[CompletionUsage]
