# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from typing_extensions import Literal

from ..core import BaseModel
from .batch_error import BatchError
from .batch_request_counts import BatchRequestCounts

__all__ = ['Batch', 'Errors']


class Errors(BaseModel):
	"""
	Batch errors information

	Attributes:
		data (Optional[List[BatchError]]): List of batch errors
		object (Optional[str]): This type is always `list`
	"""

	data: Optional[List[BatchError]] = None
	object: Optional[str] = None


class Batch(BaseModel):
	"""
	Batch processing object

	Attributes:
		id (str): Batch identifier
		completion_window (str): Address information for executing the request
		created_at (int): This is the creation time represented by the Unix timestamp (in seconds)
		endpoint (str): This is the address of the Z.ai endpoint
		input_file_id (str): The ID of the input file marked as batch
		object (Literal['batch']): This type is always `batch`
		status (Literal): The status of the batch
		cancelled_at (Optional[int]): The cancellation time represented by the Unix timestamp (in seconds)
		cancelling_at (Optional[int]): The time when the cancellation request was initiated,
										represented by the Unix timestamp (in seconds)
		completed_at (Optional[int]): The completion time represented by the Unix timestamp (in seconds)
		error_file_id (Optional[str]): This file ID contains the output of the request that failed to be executed
		errors (Optional[Errors]): Batch errors information
		expired_at (Optional[int]): The expiration time represented by the Unix timestamp (in seconds)
		expires_at (Optional[int]): The expiration is triggered by the Unix timestamp (in seconds)
		failed_at (Optional[int]): The failure time represented by the Unix timestamp (in seconds)
		finalizing_at (Optional[int]): The final time represented by the Unix timestamp (in seconds)
		in_progress_at (Optional[int]): The start processing time represented by the Unix timestamp (in seconds)
		metadata (Optional[builtins.object]): Metadata in key:value format to store information in a structured format.
										The key length is 64 characters, and the value is up to 512 characters long
		output_file_id (Optional[str]): The ID of the output file for the completed request
		request_counts (Optional[BatchRequestCounts]): Request count for different states in the batch
	"""

	id: str
	completion_window: str
	created_at: int
	endpoint: str
	input_file_id: str
	object: Literal['batch']
	status: Literal[
		'validating',
		'failed',
		'in_progress',
		'finalizing',
		'completed',
		'expired',
		'cancelling',
		'cancelled',
	]

	cancelled_at: Optional[int] = None
	cancelling_at: Optional[int] = None
	completed_at: Optional[int] = None
	error_file_id: Optional[str] = None
	errors: Optional[Errors] = None
	expired_at: Optional[int] = None
	expires_at: Optional[int] = None
	failed_at: Optional[int] = None
	finalizing_at: Optional[int] = None
	in_progress_at: Optional[int] = None
	metadata: Optional[builtins.object] = None
	output_file_id: Optional[str] = None
	request_counts: Optional[BatchRequestCounts] = None
