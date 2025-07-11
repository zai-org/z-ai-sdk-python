from typing import Dict, List, Optional, TypedDict

__all__ = ['DocumentEditParams']


class DocumentEditParams(TypedDict):
	"""
	Knowledge parameter type definition

	Attributes:
	    id (str): Knowledge ID
	    knowledge_type (int): Knowledge type:
	                    1: Article knowledge: supports pdf,url,docx
	                    2: Q&A knowledge-document: supports pdf,url,docx
	                    3: Q&A knowledge-table: supports xlsx
	                    4: Product library-table: supports xlsx
	                    5: Custom: supports pdf,url,docx
	    custom_separator (Optional[List[str]]): Slice rules when current knowledge type is custom
	                                            (knowledge_type=5), default \n
	    sentence_size (Optional[int]): Slice word count when current knowledge type is custom
	                                   (knowledge_type=5), value range: 20-2000, default 300
	    callback_url (Optional[str]): Callback address
	    callback_header (Optional[dict]): Header carried during callback
	"""

	id: str
	knowledge_type: int
	custom_separator: Optional[List[str]]
	sentence_size: Optional[int]
	callback_url: Optional[str]
	callback_header: Optional[Dict[str, str]]
