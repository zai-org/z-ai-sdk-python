from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

from ...types.sensitive_word_check import SensitiveWordCheckRequest

__all__ = ['WebSearchCreatParams']


class WebSearchCreatParams(TypedDict):
	"""
	Web search creation parameters

	Attributes:
		search_engine (str): Search engine
		search_query (str): Search query text
		request_id (str): Passed by the user, must be unique; used to distinguish the unique identifier
			of each request, the platform will generate it by default when the user does not
			pass it.
		user_id (str): User side.
		sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
	"""

	search_engine: str
	search_query: str
	request_id: str
	user_id: str
	sensitive_word_check: Optional[SensitiveWordCheckRequest]
