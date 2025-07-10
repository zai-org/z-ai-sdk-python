from typing import List, Optional

from ...core import BaseModel
from .web_search import SearchIntent, SearchRecommend, SearchResult

__all__ = ['WebSearchChunk']


class ChoiceDeltaToolCall(BaseModel):
	"""
	Represents a tool call delta in web search streaming responses.

	Attributes:
		index (int): The index of the tool call
		id (Optional[str]): Unique identifier for the tool call
		search_intent (Optional[SearchIntent]): Search intent information
		search_result (Optional[SearchResult]): Search result data
		search_recommend (Optional[SearchRecommend]): Search recommendations
		type (Optional[str]): Type of the tool call
	"""
	index: int
	id: Optional[str] = None

	search_intent: Optional[SearchIntent] = None
	search_result: Optional[SearchResult] = None
	search_recommend: Optional[SearchRecommend] = None
	type: Optional[str] = None


class ChoiceDelta(BaseModel):
	"""
	Represents the delta changes in a streaming choice.

	Attributes:
		role (Optional[str]): The role of the message sender
		tool_calls (Optional[List[ChoiceDeltaToolCall]]): List of tool call deltas
	"""
	role: Optional[str] = None
	tool_calls: Optional[List[ChoiceDeltaToolCall]] = None


class Choice(BaseModel):
	"""
	Represents a choice in the web search streaming response.

	Attributes:
		delta (ChoiceDelta): The delta changes for this choice
		finish_reason (Optional[str]): Reason why the generation finished
		index (int): Index of this choice in the response
	"""
	delta: ChoiceDelta
	finish_reason: Optional[str] = None
	index: int


class WebSearchChunk(BaseModel):
	"""
	Represents a chunk in the web search streaming response.

	Attributes:
		id (Optional[str]): Unique identifier for the chunk
		choices (List[Choice]): List of choices in this chunk
		created (Optional[int]): Timestamp when the chunk was created
	"""
	id: Optional[str] = None
	choices: List[Choice]
	created: Optional[int] = None
