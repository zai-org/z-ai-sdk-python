from __future__ import annotations

import os
from functools import cached_property
from typing import TYPE_CHECKING, Mapping, Union

import httpx
from httpx import Timeout
from typing_extensions import override

if TYPE_CHECKING:
	from zai.api_resource.agents import Agents
	from zai.api_resource.assistant import Assistant
	from zai.api_resource.audio import Audio
	from zai.api_resource.batches import Batches
	from zai.api_resource.chat import Chat
	from zai.api_resource.embeddings import Embeddings
	from zai.api_resource.files import Files
	from zai.api_resource.fine_tuning import FineTuning
	from zai.api_resource.images import Images
	from zai.api_resource.knowledge import Knowledge
	from zai.api_resource.moderations import Moderations
	from zai.api_resource.tools import Tools
	from zai.api_resource.videos import Videos
	from zai.api_resource.web_search import WebSearchApi

from .core import (
	NOT_GIVEN,
	ZAI_DEFAULT_MAX_RETRIES,
	HttpClient,
	NotGiven,
	ZaiError,
	_jwt_token,
)


class ZaiClient(HttpClient):
	"""
	Main client for interacting with the ZAI API

	Attributes:
		chat (Chat): Chat completions API resource
		api_key (str): API key for authentication
		_disable_token_cache (bool): Whether to disable token caching
		source_channel (str): Source channel identifier
	"""

	chat: Chat
	api_key: str
	_disable_token_cache: bool = True
	source_channel: str

	def __init__(
		self,
		*,
		api_key: str | None = None,
		base_url: str | httpx.URL | None = None,
		timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
		max_retries: int = ZAI_DEFAULT_MAX_RETRIES,
		http_client: httpx.Client | None = None,
		custom_headers: Mapping[str, str] | None = None,
		disable_token_cache: bool = True,
		_strict_response_validation: bool = False,
		source_channel: str | None = None,
		switch_to_zhipu: bool = False,
	) -> None:
		"""
		Initialize the ZAI client

		Arguments:
			api_key (str | None): API key for authentication.
									If None, will try to get from ZAI_API_KEY environment variable.
			base_url (str | httpx.URL | None): Base URL for the API.
									If None, will try to get from ZAI_BASE_URL environment variable
			timeout (Union[float, Timeout, None, NotGiven]): Request timeout configuration
			max_retries (int): Maximum number of retries for failed requests
			http_client (httpx.Client | None): Custom HTTP client to use
			custom_headers (Mapping[str, str] | None): Additional headers to include in requests
			disable_token_cache (bool): Whether to disable JWT token caching
			_strict_response_validation (bool): Whether to enable strict response validation
			source_channel (str | None): Source channel identifier
			switch_to_zhipu (bool): Whether to switch to Zhipu base_url
		"""
		if api_key is None:
			api_key = os.environ.get('ZAI_API_KEY')
		if api_key is None:
			raise ZaiError('api_key not provided, please provide it through parameters or environment variables')
		self.api_key = api_key
		self.source_channel = source_channel
		self._disable_token_cache = disable_token_cache

		if base_url is None:
			base_url = os.environ.get('ZAI_BASE_URL')
		if base_url is None:
			base_url = 'https://api.z.ai/api/paas/v4'
		if switch_to_zhipu:
			base_url = 'https://open.bigmodel.cn/api/paas/v4'
		from ._version import __version__

		super().__init__(
			version=__version__,
			base_url=base_url,
			max_retries=max_retries,
			timeout=timeout,
			custom_httpx_client=http_client,
			custom_headers=custom_headers,
			_strict_response_validation=_strict_response_validation,
		)

	@cached_property
	def chat(self) -> Chat:
		from zai.api_resource.chat import Chat

		return Chat(self)

	@cached_property
	def assistant(self) -> Assistant:
		from zai.api_resource.assistant import Assistant

		return Assistant(self)

	@cached_property
	def agents(self) -> Agents:
		from zai.api_resource.agents import Agents

		return Agents(self)

	@cached_property
	def embeddings(self) -> Embeddings:
		from zai.api_resource.embeddings import Embeddings

		return Embeddings(self)

	@cached_property
	def fine_tuning(self) -> FineTuning:
		from zai.api_resource.fine_tuning import FineTuning

		return FineTuning(self)

	@cached_property
	def batches(self) -> Batches:
		from zai.api_resource.batches import Batches

		return Batches(self)

	@cached_property
	def knowledge(self) -> Knowledge:
		from zai.api_resource.knowledge import Knowledge

		return Knowledge(self)

	@cached_property
	def tools(self) -> Tools:
		from zai.api_resource.tools import Tools

		return Tools(self)

	@cached_property
	def web_search(self) -> WebSearchApi:
		from zai.api_resource.web_search import WebSearchApi

		return WebSearchApi(self)

	@cached_property
	def files(self) -> Files:
		from zai.api_resource.files import Files

		return Files(self)

	@cached_property
	def images(self) -> Images:
		from zai.api_resource.images import Images

		return Images(self)

	@cached_property
	def audio(self) -> Audio:
		from zai.api_resource.audio import Audio

		return Audio(self)

	@cached_property
	def videos(self) -> Videos:
		from zai.api_resource.videos import Videos

		return Videos(self)

	@cached_property
	def moderations(self) -> Moderations:
		from zai.api_resource.moderations import Moderations

		return Moderations(self)

	@property
	@override
	def auth_headers(self) -> dict[str, str]:
		api_key = self.api_key
		source_channel = self.source_channel or 'python-sdk'
		if self._disable_token_cache:
			return {
				'Authorization': f'Bearer {api_key}',
				'x-source-channel': source_channel,
			}
		else:
			return {
				'Authorization': f'Bearer {_jwt_token.generate_token(api_key)}',
				'x-source-channel': source_channel,
			}

	def __del__(self) -> None:
		if not hasattr(self, '_has_custom_http_client') or not hasattr(self, 'close') or not hasattr(self, '_client'):
			# if the '__init__' method raised an error, self would not have client attr
			return

		if self._has_custom_http_client:
			return

		self.close()
