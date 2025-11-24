from typing import List
from typing import Optional

from zai.core import BaseModel

__all__ = ["HandwritingOCRResp"]


class Location(BaseModel):
    left: int
    top: int
    width: int
    height: int


class Probability(BaseModel):
    average: float
    variance: float
    min: float


class WordsResult(BaseModel):
    location: Location
    words: str
    probability: Probability


class HandwritingOCRResp(BaseModel):
    task_id: str  # Task ID or Result ID
    message: str  # Status message
    status: str  # OCR task status
    words_result_num: int  # Number of recognition results
    words_result: Optional[List[WordsResult]] = None  # List of recognition resultst details (if any)
