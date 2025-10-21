from typing import List, Optional

from zai.core import BaseModel

__all__ = [
    "FileParserTaskCreateResp"
]


class FileParserTaskCreateResp(BaseModel):
    task_id: str
    # Task ID
    message: str
    # Message
    success: bool
    # Whether successful
