from typing import List, Optional

from ...core import BaseModel

__all__ = ['FileObject', 'ListOfFileObject']


class FileObject(BaseModel):
	"""
	Represents a file object in the system.

	Attributes:
		id (Optional[str]): Unique identifier for the file
		bytes (Optional[int]): Size of the file in bytes
		created_at (Optional[int]): Timestamp when the file was created
		filename (Optional[str]): Name of the file
		object (Optional[str]): Object type identifier
		purpose (Optional[str]): Purpose of the file
		status (Optional[str]): Current status of the file
		status_details (Optional[str]): Additional details about the file status
	"""
	id: Optional[str] = None
	bytes: Optional[int] = None
	created_at: Optional[int] = None
	filename: Optional[str] = None
	object: Optional[str] = None
	purpose: Optional[str] = None
	status: Optional[str] = None
	status_details: Optional[str] = None


class ListOfFileObject(BaseModel):
	"""
	Represents a paginated list of file objects.

	Attributes:
		object (Optional[str]): Object type identifier
		data (List[FileObject]): List of file objects
		has_more (Optional[bool]): Whether there are more files available
	"""
	object: Optional[str] = None
	data: List[FileObject]
	has_more: Optional[bool] = None
