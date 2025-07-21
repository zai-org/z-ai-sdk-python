from __future__ import annotations

from typing import List, Optional

from ..core import BaseModel
from .chat.chat_completion import CompletionUsage

__all__ = ['Embedding', 'EmbeddingsResponded']


class Embedding(BaseModel):
	"""
	Embedding vector data

	Attributes:
		object (str): Object type identifier
		index (Optional[int]): Index of the embedding in the list
		embedding (List[float]): The embedding vector
	"""

	object: str
	index: Optional[int] = None
	embedding: List[float]


class EmbeddingsResponded(BaseModel):
	"""
	Embeddings generation response

	Attributes:
		object (str): Object type identifier
		data (List[Embedding]): List of embedding vectors
		model (str): Model used for embedding generation
		usage (CompletionUsage): Token usage information
	"""

	object: str
	data: List[Embedding]
	model: str
	usage: CompletionUsage
