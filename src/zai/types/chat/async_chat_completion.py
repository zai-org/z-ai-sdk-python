from typing import List, Optional

from ...core import BaseModel
from .chat_completion import CompletionChoice, CompletionUsage

__all__ = ['AsyncTaskStatus', 'AsyncCompletion']


class AsyncTaskStatus(BaseModel):
	"""
	Represents the status of an asynchronous task.

	Attributes:
		id (Optional[str]): Unique identifier for the task
		request_id (Optional[str]): Unique identifier for the request
		model (Optional[str]): Model used for the task
		task_status (Optional[str]): Current status of the task
	"""
	id: Optional[str] = None
	request_id: Optional[str] = None
	model: Optional[str] = None
	task_status: Optional[str] = None


class AsyncCompletion(BaseModel):
	"""
	Represents an asynchronous completion response.

	Attributes:
		id (Optional[str]): Unique identifier for the completion
		request_id (Optional[str]): Unique identifier for the request
		model (Optional[str]): Model used for the completion
		task_status (str): Current status of the task
		choices (List[CompletionChoice]): List of completion choices
		usage (CompletionUsage): Token usage statistics
	"""
	id: Optional[str] = None
	request_id: Optional[str] = None
	model: Optional[str] = None
	task_status: str
	choices: List[CompletionChoice]
	usage: CompletionUsage
