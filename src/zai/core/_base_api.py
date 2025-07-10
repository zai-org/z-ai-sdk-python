from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .._client import ZaiClient


class BaseAPI:
	"""
	Base class for all API resource classes.

	Provides common functionality and HTTP method shortcuts for API resources.
	All API resource classes should inherit from this base class.

	Attributes:
		_client (ZaiClient): The client instance for making API requests
	"""
	_client: ZaiClient

	def __init__(self, client: ZaiClient) -> None:
		"""
		Initialize the API resource with a client instance.

		Args:
			client (ZaiClient): The client instance for making API requests
		"""
		self._client = client
		self._delete = client.delete
		self._get = client.get
		self._post = client.post
		self._put = client.put
		self._patch = client.patch
		self._get_api_list = client.get_api_list
