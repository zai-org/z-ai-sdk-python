from __future__ import annotations

from typing import List

from zai.core import BaseModel
from zai.types.knowledge.document.document import DocumentData


class DocumentPage(BaseModel):
	list: List[DocumentData]
	object: str
