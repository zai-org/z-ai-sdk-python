from typing import Optional

from ...core import BaseModel

__all__ = ['KnowledgeStatistics', 'KnowledgeUsed']


class KnowledgeStatistics(BaseModel):
	"""
	Usage statistics
	"""

	word_num: Optional[int] = None
	length: Optional[int] = None


class KnowledgeUsed(BaseModel):
	used: Optional[KnowledgeStatistics] = None
	"""Used amount"""
	total: Optional[KnowledgeStatistics] = None
	"""Total knowledge base"""
