from typing import List, Optional

from ...core import BaseModel

__all__ = ['Completion', 'CompletionUsage']


class Function(BaseModel):
	"""
	Function call information
	
	Attributes:
		arguments: Function call arguments
		name: Function name
	"""
	arguments: str
	name: str


class CompletionMessageToolCall(BaseModel):
	"""
	Tool call information in completion message
	
	Attributes:
		id: Unique identifier for the tool call
		function: Function call information
		type: Type of the tool call
	"""
	id: str
	function: Function
	type: str


class CompletionMessage(BaseModel):
	"""
	Completion message information
	
	Attributes:
		content: Message content
		role: Role of the message sender
		reasoning_content: Reasoning content
		tool_calls: List of tool calls in the message
	"""
	content: Optional[str] = None
	role: str
	reasoning_content: Optional[str] = None
	tool_calls: Optional[List[CompletionMessageToolCall]] = None


class CompletionUsage(BaseModel):
	"""
	Token usage information for completion
	
	Attributes:
		prompt_tokens: Number of tokens in the prompt
		completion_tokens: Number of tokens in the completion
		total_tokens: Total number of tokens used
	"""
	prompt_tokens: int
	completion_tokens: int
	total_tokens: int


class CompletionChoice(BaseModel):
	"""
	Completion choice information
	
	Attributes:
		index: Index of the choice
		finish_reason: Reason why the completion finished
		message: Completion message
	"""
	index: int
	finish_reason: str
	message: CompletionMessage


class Completion(BaseModel):
	"""
	Chat completion response
	
	Attributes:
		model: Model used for the completion
		created: Timestamp when the completion was created
		choices: List of completion choices
		request_id: Request identifier
		id: Unique identifier for the completion
		usage: Token usage information
	"""
	model: Optional[str] = None
	created: Optional[int] = None
	choices: List[CompletionChoice]
	request_id: Optional[str] = None
	id: Optional[str] = None
	usage: CompletionUsage
