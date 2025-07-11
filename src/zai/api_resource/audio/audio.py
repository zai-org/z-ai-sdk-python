from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Optional, cast

import httpx

from zai.core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	FileTypes,
	Headers,
	NotGiven,
	deepcopy_minimal,
	make_request_options,
	maybe_transform,
)
from zai.core._legacy_binary_response import HttpxBinaryResponseContent
from zai.core._utils import extract_files
from zai.types.audio import AudioSpeechParams
from zai.types.sensitive_word_check import SensitiveWordCheckRequest

from ...core import cached_property
from ...types.audio import audio_customization_param
from .transcriptions import Transcriptions

if TYPE_CHECKING:
	from zai._client import ZaiClient

__all__ = ['Audio']


class Audio(BaseAPI):
	"""
	API resource for audio operations
	
	Attributes:
		transcriptions (Transcriptions): Audio transcription operations
	"""
	@cached_property
	def transcriptions(self) -> Transcriptions:
		return Transcriptions(self._client)

	def __init__(self, client: 'ZaiClient') -> None:
		super().__init__(client)

	def speech(
		self,
		*,
		model: str,
		input: str = None,
		voice: str = None,
		response_format: str = None,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		request_id: str = None,
		user_id: str = None,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> HttpxBinaryResponseContent:
		"""
		Generate speech audio from text input
		
		Arguments:
			model (str): The model to use for speech generation
			input (str): The text to convert to speech
			voice (str): The voice to use for speech generation
			response_format (str): The format of the response audio
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
			request_id (str): Unique identifier for the request
			user_id (str): User identifier
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		body = deepcopy_minimal(
			{
				'model': model,
				'input': input,
				'voice': voice,
				'response_format': response_format,
				'sensitive_word_check': sensitive_word_check,
				'request_id': request_id,
				'user_id': user_id,
			}
		)
		return self._post(
			'/audio/speech',
			body=maybe_transform(body, AudioSpeechParams),
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=HttpxBinaryResponseContent,
		)

	def customization(
		self,
		*,
		model: str,
		input: str = None,
		voice_text: str = None,
		voice_data: FileTypes = None,
		response_format: str = None,
		sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
		request_id: str = None,
		user_id: str = None,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> HttpxBinaryResponseContent:
		"""
		Generate customized speech audio with voice cloning
		
		Arguments:
			model (str): The model to use for speech generation
			input (str): The text to convert to speech
			voice_text (str): Text for voice customization
			voice_data (FileTypes): Voice data file for customization
			response_format (str): The format of the response audio
			sensitive_word_check (Optional[SensitiveWordCheckRequest]): Sensitive word check configuration
			request_id (str): Unique identifier for the request
			user_id (str): User identifier
			extra_headers (Headers): Additional headers to send
			extra_body (Body): Additional body parameters
			timeout (float | httpx.Timeout): Request timeout
		"""
		body = deepcopy_minimal(
			{
				'model': model,
				'input': input,
				'voice_text': voice_text,
				'voice_data': voice_data,
				'response_format': response_format,
				'sensitive_word_check': sensitive_word_check,
				'request_id': request_id,
				'user_id': user_id,
			}
		)
		files = extract_files(cast(Mapping[str, object], body), paths=[['voice_data']])

		if files:
			extra_headers = {
				'Content-Type': 'multipart/form-data',
				**(extra_headers or {}),
			}
		return self._post(
			'/audio/customization',
			body=maybe_transform(body, audio_customization_param.AudioCustomizationParam),
			files=files,
			options=make_request_options(extra_headers=extra_headers, extra_body=extra_body, timeout=timeout),
			cast_type=HttpxBinaryResponseContent,
		)
