from typing import List, Optional

from zai.core import BaseModel

__all__ = [
    "FileParserTaskCreateResp"
]


class FileParserTaskCreateResp(BaseModel):
    task_id: str
    # 任务id
    message: str
    # message
    success: bool
    # 是否成功
