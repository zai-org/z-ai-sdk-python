from typing import Any, Dict, List, Optional

from ...core import BaseModel

__all__ = [
	'CompletionUsage',
	'ChatCompletionChunk',
	'Choice',
	'ChoiceDelta',
	'ChoiceDeltaFunctionCall',
	'ChoiceDeltaToolCall',
	'ChoiceDeltaToolCallFunction',
	'AudioCompletionChunk',
]


class ChoiceDeltaFunctionCall(BaseModel):
	"""
	Function call delta information in streaming response
	
	Attributes:
		arguments: Function call arguments
		name: Function name
	"""
	arguments: Optional[str] = None
	name: Optional[str] = None


class ChoiceDeltaToolCallFunction(BaseModel):
	"""
	Tool call function delta information in streaming response
	
	Attributes:
		arguments: Function call arguments
		name: Function name
	"""
	arguments: Optional[str] = None
	name: Optional[str] = None


class ChoiceDeltaToolCall(BaseModel):
	"""
	Tool call delta information in streaming response
	
	Attributes:
		index: Index of the tool call
		id: Unique identifier for the tool call
		function: Function call information
		type: Type of the tool call
	"""
	index: int
	id: Optional[str] = None
	function: Optional[ChoiceDeltaToolCallFunction] = None
	type: Optional[str] = None


class AudioCompletionChunk(BaseModel):
	"""
	Audio completion chunk information
	
	Attributes:
		id: Unique identifier for the audio chunk
		data: Audio data content
		expires_at: Timestamp when the audio expires
	"""
	id: Optional[str] = None
	data: Optional[str] = None
	expires_at: Optional[int] = None


class ChoiceDelta(BaseModel):
	"""
	Delta information for streaming chat completion choice
	
	Attributes:
		content: Content delta
		role: Role of the message sender
		reasoning_content: Reasoning content delta
		tool_calls: List of tool call deltas
		audio: Audio completion chunk
	"""
	content: Optional[str] = None
	role: Optional[str] = None
	reasoning_content: Optional[str] = None
	tool_calls: Optional[List[ChoiceDeltaToolCall]] = None
	audio: Optional[AudioCompletionChunk] = None


class Choice(BaseModel):
	"""
	Choice information in streaming chat completion
	
	Attributes:
		delta: Delta information for the choice
		finish_reason: Reason why the completion finished
		index: Index of the choice
	"""
	delta: ChoiceDelta
	finish_reason: Optional[str] = None
	index: int


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


class ChatCompletionChunk(BaseModel):
	"""
	Streaming chat completion chunk response
	
	Attributes:
		id: Unique identifier for the completion
		choices: List of completion choices
		created: Timestamp when the completion was created
		model: Model used for the completion
		usage: Token usage information
		extra_json: Additional JSON data
	"""
	id: Optional[str] = None
	choices: List[Choice]
	created: Optional[int] = None
	model: Optional[str] = None
	usage: Optional[CompletionUsage] = None
	extra_json: Dict[str, Any]
