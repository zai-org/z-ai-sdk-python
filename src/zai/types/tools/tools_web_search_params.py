from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypedDict

__all__ = ['WebSearchParams']


class WebSearchParams(TypedDict):
	"""
	Tool name: web-search-pro parameter type definition

	Attributes:
	    :param model: str, model name
	    :param request_id: Optional[str], request ID
	    :param stream: Optional[bool], whether to stream
	    :param messages: Union[str, List[str], List[int], object, None],
	                    Contains the content of the historical conversation context, passed in the form of a json array
	                    of {"role": "user", "content": "Hello"}
	                    The current version only supports single-turn conversations with User Message.
	                     The tool will understand
	                    the User Message and perform a search.
	                    Please try to pass in the user's original question without instruction format
	                    to improve search accuracy.
	    :param scope: Optional[str], specify the search scope, such as the entire network, academic, etc.,
	                    the default is the entire network
	    :param location: Optional[str], specify the user's location to improve relevance
	    :param recent_days: Optional[int], supports specifying the return of search results updated in N days (1-30)
	"""  # noqa: E101

	model: str
	request_id: Optional[str]
	stream: Optional[bool]
	messages: Union[str, List[str], List[int], object, None]
	scope: Optional[str] = None
	location: Optional[str] = None
	recent_days: Optional[int] = None
