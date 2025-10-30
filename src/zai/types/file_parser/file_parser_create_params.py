from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict
from zai.core import FileTypes

__all__ = ["FileParserCreateParams", "FileParserDownloadParams"]


class FileParserCreateParams(TypedDict):
    file: FileTypes
    """Uploaded file"""
    file_type: str
    """File type"""
    tool_type: Literal["lite", "expert", "prime"]
    """Tool type"""


class FileParserDownloadParams(TypedDict):
    task_id: str
    """Parsing task id"""
    format_type: Literal["text", "download_link"]
    """Result return type"""

class FileParserSyncParams(TypedDict):
    file: FileTypes
    """Uploaded file"""
    file_type: str
    """File type"""
    tool_type: Literal["prime-sync"]
    """Tool type"""
