from __future__ import annotations

from typing import List

from ....core import BaseModel
from . import DocumentData

__all__ = ['DocumentPage']


class DocumentPage(BaseModel):
	list: List[DocumentData]
	object: str
