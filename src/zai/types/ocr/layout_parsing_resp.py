from typing import List, Optional, Dict, Any

from zai.core import BaseModel

__all__ = ["LayoutParsingResp", "LayoutDetail", "DataInfo", "PageInfo", "Usage"]


class Usage(BaseModel):
    """Token usage information"""
    completion_tokens: int
    prompt_tokens: int
    prompt_tokens_details: Optional[Dict[str, Any]] = None
    total_tokens: int


class PageInfo(BaseModel):
    """Page size information"""
    width: int
    height: int


class DataInfo(BaseModel):
    """Document basic information"""
    num_pages: int
    pages: Optional[List[PageInfo]] = None


class LayoutDetail(BaseModel):
    """Layout detail element"""
    index: int
    label: str
    bbox_2d: Optional[List[float]] = None
    content: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None


class LayoutParsingResp(BaseModel):
    """Response model for layout parsing API"""
    id: str
    created: int
    model: str
    md_results: Optional[str] = None
    layout_details: Optional[List[List[LayoutDetail]]] = None
    layout_visualization: Optional[List[str]] = None
    data_info: Optional[DataInfo] = None
    usage: Optional[Usage] = None
    request_id: Optional[str] = None
