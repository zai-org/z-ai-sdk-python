from typing import Optional

from ...core import BaseModel

__all__ = [
	'SearchIntentResp',
	'SearchResultResp',
]


class SearchIntentResp(BaseModel):
    """
    Search intent response

    Attributes:
        query (str): Search optimized query
        intent (str): Determined intent type
        keywords (str): Search keywords
    """
    query: str
    intent: str
    keywords: str


class SearchResultResp(BaseModel):
	"""
	Search result response

	Attributes:
		title (str): Title
		link (str): Link
		content (str): Content
		icon (str): Icon
		media (str): Source media
		refer (str): Reference number [ref_1]
		publish_date (str): Publish date
	"""
	title: str
	link: str
	content: str
	icon: str
	media: str
	refer: str
	publish_date: str


class WebSearchResp(BaseModel):
	"""
	Web search response

	Attributes:
		created (Optional[int]): Creation timestamp
		request_id (Optional[str]): Request identifier
		id (Optional[str]): Response identifier
		search_intent (Optional[SearchIntentResp]): Search intent response
		search_result (Optional[SearchResultResp]): Search result response
	"""
	created: Optional[int] = None
	request_id: Optional[str] = None
	id: Optional[str] = None
	search_intent: Optional[SearchIntentResp]
	search_result: Optional[SearchResultResp]
