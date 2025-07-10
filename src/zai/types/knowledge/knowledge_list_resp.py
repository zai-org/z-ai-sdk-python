from __future__ import annotations

from typing import List

from ...core import BaseModel
from . import KnowledgeInfo

__all__ = ['KnowledgePage']


class KnowledgePage(BaseModel):
	list: List[KnowledgeInfo]
	object: str
