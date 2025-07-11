from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Dict, List, Optional, Union

import httpx
from typing_extensions import Literal

from ...core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	Headers,
	NotGiven,
	drop_prefix_image_data,
	make_request_options,
	maybe_transform,
)
from ...types.chat.async_chat_completion import AsyncCompletion, AsyncTaskStatus
from ...types.chat.code_geex import code_geex_params
from ...types.sensitive_word_check import SensitiveWordCheckRequest

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
	from ..._client import ZaiClient


class AsyncCompletions(BaseAPI):
	"""
	Asynchronous chat completions API resource

	Provides access to asynchronous chat completion operations.
	"""
	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def create(
		self,
		*,
		model: str,
		request_id: Optional[str] | NotGiven = NOT_GIVEN,
		user_id: Optional[str] | NotGiven = NOT_GIVEN,
		do_sample: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
		temperature: Optional[float] | NotGiven = NOT_GIVEN,
		top_p: Optional[float] | NotGiven = NOT_GIVEN,
		max_tokens: int | NotGiven = NOT_GIVEN,
		seed: int | NotGiven = NOT_GIVEN,
		messages: Union[str, List[str], List[int], List[List[int]], None],
		stop: Optional[Union[str, List[str], None]] | NotGiven = NOT_GIVEN,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		tools: Optional[object] | NotGiven = NOT_GIVEN,
		tool_choice: str | NotGiven = NOT_GIVEN,
		meta: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
		extra: Optional[code_geex_params.CodeGeexExtra] | NotGiven = NOT_GIVEN,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> AsyncTaskStatus:
		"""
		Create an asynchronous chat completion task
		
		Arguments:
			model (str): Model name to use for completion
			request_id (Optional[str]): Request identifier
			user_id (Optional[str]): User identifier
			do_sample (Optional[bool]): Whether to use sampling
			temperature (Optional[float]): Sampling temperature (0.0, 1.0)
			top_p (Optional[float]): Top-p sampling parameter (0.0, 1.0)
			max_tokens (int): Maximum number of tokens to generate
			seed (int): Random seed for reproducible results
			messages (Union[str, List[str], List[int], List[List[int]], None]): Input messages
			stop (Optional[Union[str, List[str], None]]): Stop sequences
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word checking configuration
			tools (Optional[object]): Tools available to the model
			tool_choice (str): Tool choice strategy
			meta (Optional[Dict[str, str]]): Additional metadata
			extra (Optional[CodeGeexExtra]): Extra parameters for CodeGeex models
			extra_headers (Headers): Additional HTTP headers
			extra_body (Body): Additional request body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		_cast_type = AsyncTaskStatus
		logger.debug(f'temperature:{temperature}, top_p:{top_p}')
		if temperature is not None and temperature != NOT_GIVEN:
			if temperature <= 0:
				do_sample = False
				temperature = 0.01
				# logger.warning("temperature: value range is (0.0, 1.0) open interval,"
				# "do_sample rewritten as false (parameters top_p temperature do not take effect)")
			if temperature >= 1:
				temperature = 0.99
				# logger.warning("temperature: value range is (0.0, 1.0) open interval")
		if top_p is not None and top_p != NOT_GIVEN:
			if top_p >= 1:
				top_p = 0.99
				# logger.warning("top_p: value range is (0.0, 1.0) open interval, cannot equal 0 or 1")
			if top_p <= 0:
				top_p = 0.01
				# logger.warning("top_p: value range is (0.0, 1.0) open interval, cannot equal 0 or 1")

		logger.debug(f'temperature:{temperature}, top_p:{top_p}')
		if isinstance(messages, List):
			for item in messages:
				if item.get('content'):
					item['content'] = drop_prefix_image_data(item['content'])

		body = {
			'model': model,
			'request_id': request_id,
			'user_id': user_id,
			'temperature': temperature,
			'top_p': top_p,
			'do_sample': do_sample,
			'max_tokens': max_tokens,
			'seed': seed,
			'messages': messages,
			'stop': stop,
			'sensitive_word_check': sensitive_word_check,
			'tools': tools,
			'tool_choice': tool_choice,
			'meta': meta,
			'extra': maybe_transform(extra, code_geex_params.CodeGeexExtra),
		}
		return self._post(
			'/async/chat/completions',
			body=body,
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=_cast_type,
			stream=False,
		)

	def retrieve_completion_result(
		self,
		id: str,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> Union[AsyncCompletion, AsyncTaskStatus]:
		"""
		Retrieve the result of an asynchronous chat completion task
		
		Arguments:
			id (str): The task ID to retrieve results for
			extra_headers (Headers): Additional HTTP headers
			extra_body (Body): Additional request body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		_cast_type = Union[AsyncCompletion, AsyncTaskStatus]
		return self._get(
			path=f'/async-result/{id}',
			cast_type=_cast_type,
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
		)
