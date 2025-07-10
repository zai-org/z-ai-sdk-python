from typing import List, Optional

from ....core import BaseModel

__all__ = [
	'DocumentData',
	'DocumentObject',
	'DocumentSuccessinfo',
	'DocumentFailedInfo',
]


class DocumentSuccessinfo(BaseModel):
	"""
	Represents successful document upload information.

	Attributes:
		documentId (Optional[str]): Document ID
		filename (Optional[str]): Document filename
	"""

	documentId: Optional[str] = None
	filename: Optional[str] = None


class DocumentFailedInfo(BaseModel):
	"""
	Represents failed document upload information.

	Attributes:
		failReason (Optional[str]): Reason for upload failure, including: unsupported file format,
								file size exceeds limit, knowledge base capacity is full,
								capacity limit is 500,000 words
		filename (Optional[str]): Document filename
		documentId (Optional[str]): Knowledge base ID
	"""

	failReason: Optional[str] = None
	filename: Optional[str] = None
	documentId: Optional[str] = None


class DocumentObject(BaseModel):
	"""
	Document information

	Attributes:
		successInfos (Optional[List[DocumentSuccessinfo]]): Information about successfully uploaded files
		failedInfos (Optional[List[DocumentFailedInfo]]): Information about failed file uploads
	"""

	successInfos: Optional[List[DocumentSuccessinfo]] = None
	failedInfos: Optional[List[DocumentFailedInfo]] = None


class DocumentDataFailInfo(BaseModel):
	"""
	Document vectorization failure information

	Attributes:
		embedding_code (Optional[int]): Error code (10001: Knowledge unavailable, knowledge base space limit reached;
										10002: Knowledge unavailable, word count exceeded)
		embedding_msg (Optional[str]): Failure reason description
	"""

	embedding_code: Optional[int] = None
	embedding_msg: Optional[str] = None


class DocumentData(BaseModel):
	"""
	Document data information

	Attributes:
		id (str): Unique knowledge document identifier
		custom_separator (List[str]): Custom text slicing rules
		sentence_size (str): Text slice size configuration
		length (int): File size in bytes
		word_num (int): Total word count in the file
		name (str): Document file name
		url (str): File download URL
		embedding_stat (int): Vectorization status (0: vectorizing, 1: completed, 2: failed)
		failInfo (Optional[DocumentDataFailInfo]): Failure information when vectorization fails (embedding_stat=2)
	"""

	id: str = None
	custom_separator: List[str] = None
	sentence_size: str = None
	length: int = None
	word_num: int = None
	name: str = None
	url: str = None
	embedding_stat: int = None
	failInfo: Optional[DocumentDataFailInfo] = None
