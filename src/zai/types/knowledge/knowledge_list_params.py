from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ['KnowledgeListParams']


class KnowledgeListParams(TypedDict, total=False):
	"""
	Parameters for listing knowledge resources.

	Attributes:
		page (int): Page number, default 1, first page
		size (int): Number per page, default 10
	"""

	page: int = 1
	size: int = 10
