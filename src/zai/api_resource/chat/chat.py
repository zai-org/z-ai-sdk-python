from typing import TYPE_CHECKING

from ...core import BaseAPI, cached_property
from .async_completions import AsyncCompletions
from .completions import Completions

if TYPE_CHECKING:
	pass


class Chat(BaseAPI):
	"""
	API resource for chat operations.

	Provides access to chat completions and async completions.
	"""
	@cached_property
	def completions(self) -> Completions:
		return Completions(self._client)

	@cached_property
	def asyncCompletions(self) -> AsyncCompletions:
		return AsyncCompletions(self._client)
