from typing import List, Optional

from zai.core import BaseModel

__all__ = ["FileParserTaskCreateResp", "FileParsingDownloadResp"]


class FileParserTaskCreateResp(BaseModel):
    task_id: str
    # Task ID
    message: str
    # Message
    success: bool
    # Whether successful


class FileParsingDownloadResp(BaseModel):
    task_id: str
    # Task ID
    message: str
    # Message
    status: bool
    # Whether successful
    content: str
    # Parsed result text content
    parsing_result_url: str
    # Parsed result download link
