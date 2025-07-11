from typing import List, Optional, Union

from ...core import BaseModel

__all__ = ['FineTuningJob', 'Error', 'Hyperparameters', 'ListOfFineTuningJob']


class Error(BaseModel):
	"""
	Error information for fine-tuning job
	
	Attributes:
		code: Error code
		message: Error message description
		param: Optional parameter that caused the error
	"""
	code: str
	message: str
	param: Optional[str] = None


class Hyperparameters(BaseModel):
	"""
	Hyperparameters for fine-tuning job
	
	Attributes:
		n_epochs: Number of training epochs
	"""
	n_epochs: Union[str, int, None] = None


class FineTuningJob(BaseModel):
	"""
	Fine-tuning job information
	
	Attributes:
		id: Unique identifier for the fine-tuning job
		request_id: Request identifier
		created_at: Timestamp when the job was created
		error: Error information if the job failed
		fine_tuned_model: Name of the fine-tuned model
		finished_at: Timestamp when the job finished
		hyperparameters: Hyperparameters used for training
		model: Base model used for fine-tuning
		object: Object type identifier
		result_files: List of result file paths
		status: Current status of the fine-tuning job
		trained_tokens: Number of tokens used for training
		training_file: Path to the training file
		validation_file: Path to the validation file
	"""
	id: Optional[str] = None
	request_id: Optional[str] = None
	created_at: Optional[int] = None
	error: Optional[Error] = None
	fine_tuned_model: Optional[str] = None
	finished_at: Optional[int] = None
	hyperparameters: Optional[Hyperparameters] = None
	model: Optional[str] = None
	object: Optional[str] = None
	result_files: List[str]
	status: str
	trained_tokens: Optional[int] = None
	training_file: str
	validation_file: Optional[str] = None


class ListOfFineTuningJob(BaseModel):
	"""
	List of fine-tuning jobs response
	
	Attributes:
		object: Object type identifier
		data: List of fine-tuning job objects
	"""
	object: Optional[str] = None
	data: List[FineTuningJob]
	has_more: Optional[bool] = None
