from __future__ import annotations

from typing import List, Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = ['FileCreateParams']

from ...core import FileTypes
from . import UploadDetail


class FileCreateParams(TypedDict, total=False):
	"""
	Parameters for creating a file upload
	
	Attributes:
		file: File to upload (one of file and upload_detail is required)
		upload_detail: Upload details for multiple files (one of file and upload_detail is required)
		purpose: The purpose of uploading files, supports "fine-tune", "retrieval", and "batch"
			retrieval supports uploading Doc, Docx, PDF, Xlsx, URL type files,
        and the size of a single file does not exceed 5MB.
			fine-tune supports uploading .jsonl files and the maximum size of a single file
        is currently 100 MB. The corpus format in the file must meet the format described
        in the fine-tuning guide.
		custom_separator: When purpose is retrieval and the file type is pdf, url, docx,
                     the slicing rule defaults to `\n`
		knowledge_id: When the file upload purpose is retrieval, you need to specify the knowledge base ID to upload
		sentence_size: Sentence size parameter for retrieval purpose uploads
	"""
	file: FileTypes
	upload_detail: List[UploadDetail]
	purpose: Required[Literal['fine-tune', 'retrieval', 'batch']]
	custom_separator: Optional[List[str]]
	knowledge_id: str
	sentence_size: int
