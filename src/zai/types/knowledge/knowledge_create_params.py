from __future__ import annotations

from typing import Optional

from typing_extensions import Literal, TypedDict

__all__ = ['KnowledgeBaseParams']


class KnowledgeBaseParams(TypedDict):
	"""
	Knowledge base parameters.

	Attributes:
	    embedding_id (int): Embedding ID
	    name (str): Knowledge base name, limited to 100 characters
	    customer_identifier (Optional[str]): Customer identifier, limited to 32 characters
	    description (Optional[str]): Knowledge base description, limited to 500 characters
	    background (Optional[Literal['blue', 'red', 'orange', 'purple', 'sky']]): Background color
	    icon (Optional[Literal['question', 'book', 'seal', 'wrench', 'tag', 'horn', 'house']]): Knowledge base icon
	    bucket_id (Optional[str]): Bucket ID, limited to 32 characters
	"""

	embedding_id: int
	name: str
	customer_identifier: Optional[str]
	description: Optional[str]
	background: Optional[Literal['blue', 'red', 'orange', 'purple', 'sky']] = None
	icon: Optional[Literal['question', 'book', 'seal', 'wrench', 'tag', 'horn', 'house']] = None
	bucket_id: Optional[str]
