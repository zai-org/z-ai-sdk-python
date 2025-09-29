from typing import List, Optional

from zai.core import BaseModel

__all__ = ["FileParserTaskCreateResp", "FileParsingDownloadResp"]


class FileParserTaskCreateResp(BaseModel):
    task_id: str
    # 任务id
    message: str
    # message
    success: bool
    # 是否成功


class FileParsingDownloadResp(BaseModel):
    task_id: str
    # 任务id
    message: str
    # message
    status: bool
    # 是否成功
    content: str
    # 解析结果文本内容
    parsing_result_url: str
    # 解析结果下载链接
