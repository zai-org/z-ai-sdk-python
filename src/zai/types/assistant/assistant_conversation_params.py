from typing import TypedDict


class ConversationParameters(TypedDict, total=False):
	"""
	Parameters for conversation queries

	Attributes:
		assistant_id (str): Assistant identifier
		page (int): Current page number for pagination
		page_size (int): Number of items per page
	"""

	assistant_id: str
	page: int
	page_size: int
