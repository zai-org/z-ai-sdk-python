from typing import Optional

from zai.core import BaseModel


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
