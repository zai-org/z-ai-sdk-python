from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict


class DocumentListParams(TypedDict, total=False):
	"""
	File query parameter type definition

	Attributes:
	    purpose (Optional[str]): File purpose
	    knowledge_id (Optional[str]): When file purpose is retrieval, need to provide the knowledge base ID for query
	    page (Optional[int]): Page number, default 1
	    limit (Optional[int]): Number of files to query in the list, default 10
	    after (Optional[str]): Query file list after specified fileID (required when file purpose is fine-tune)
	    order (Optional[str]): Sort rule, optional values ['desc', 'asc'], default desc
                              (required when file purpose is fine-tune)
	"""

	purpose: Optional[str]
	knowledge_id: Optional[str]
	page: Optional[int]
	limit: Optional[int]
	after: Optional[str]
	order: Optional[str]
