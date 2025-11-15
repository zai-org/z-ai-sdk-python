from typing import Any, Dict, Optional

from pydantic import Field

from zai.core import BaseModel


class ReaderData(BaseModel):
    images: Optional[Dict[str, str]] = None
    links: Optional[Dict[str, str]] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    content: Optional[str] = None
    published_time: Optional[str] = Field(default=None, alias="publishedTime")
    metadata: Optional[Dict[str, Any]] = None
    external: Optional[Dict[str, Any]] = None


class WebReaderResult(BaseModel):
    reader_result: Optional[ReaderData] = None