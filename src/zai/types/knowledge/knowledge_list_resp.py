from __future__ import annotations

from typing import List

from zai.core import BaseModel
from zai.types.knowledge.knowledge import KnowledgeInfo


class KnowledgePage(BaseModel):
	list: List[KnowledgeInfo]
	object: str
