from __future__ import annotations

from typing_extensions import Literal, TypedDict
from zai.core import FileTypes

__all__ = ["HandwritingOCRParams"]


class HandwritingOCRParams(TypedDict, total=False):
    file: FileTypes  # Required
    tool_type: Literal["hand_write"]  # Required
    language_type: str  # Optional
    probability: bool
