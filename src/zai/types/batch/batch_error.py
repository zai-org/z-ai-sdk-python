# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..core import BaseModel

__all__ = ['BatchError']


class BatchError(BaseModel):
	"""
	Represents an error that occurred during batch processing.

	Attributes:
		code (Optional[str]): Defined business error code
		line (Optional[int]): Line number in the file where the error occurred
		message (Optional[str]): Description of the error in the conversation file
		param (Optional[str]): Parameter that caused the error
	"""

	code: Optional[str] = None
	line: Optional[int] = None
	message: Optional[str] = None
	param: Optional[str] = None
