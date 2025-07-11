from typing import List, Optional

from ...core import BaseModel

__all__ = [
	'WebSearch',
	'SearchIntent',
	'SearchResult',
	'SearchRecommend',
]


class SearchIntent(BaseModel):
	index: int
	# Search round, default is 0
	query: str
	# Search optimized query
	intent: str
	# Determined intent type
	keywords: str
	# Search keywords


class SearchResult(BaseModel):
	index: int
	# Search round, default is 0
	title: str
	# Title
	link: str
	# Link
	content: str
	# Content
	icon: str
	# Icon
	media: str
	# Source media
	refer: str
	# Reference number [ref_1]


class SearchRecommend(BaseModel):
	index: int
	# Search round, default is 0
	query: str
	# Recommended query


class WebSearchMessageToolCall(BaseModel):
	id: str
	search_intent: Optional[SearchIntent]
	search_result: Optional[SearchResult]
	search_recommend: Optional[SearchRecommend]
	type: str


class WebSearchMessage(BaseModel):
	role: str
	tool_calls: Optional[List[WebSearchMessageToolCall]] = None


class WebSearchChoice(BaseModel):
	index: int
	finish_reason: str
	message: WebSearchMessage


class WebSearch(BaseModel):
	created: Optional[int] = None
	choices: List[WebSearchChoice]
	request_id: Optional[str] = None
	id: Optional[str] = None
