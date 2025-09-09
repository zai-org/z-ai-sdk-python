from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx
from httpx import stream

from zai.core import (
	NOT_GIVEN,
	BaseAPI,
	Body,
	Headers,
	NotGiven,
	make_request_options,
	maybe_transform,
)
from zai.types.voiceclone import (
	VoiceCloneParams,
	VoiceCloneResult,
	VoiceDeleteParams,
	VoiceDeleteResult,
	VoiceListParams,
	VoiceListResult,
)

if TYPE_CHECKING:
	from zai._client import ZaiClient


class Voice(BaseAPI):
	"""
	Voice API resource for handling voice cloning operations
	"""

	def __init__(self, client: ZaiClient) -> None:
		super().__init__(client)

	def clone(
		self,
		*,
		voice_name: str,
		text: str,
		input: str,
		file_id: str,
		request_id: Optional[str] = None,
		model: str,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> VoiceCloneResult:
		"""
		Clone a voice with the provided audio sample and parameters

		Args:
			voice_name: Name for the cloned voice
			text: Text content corresponding to the sample audio
			input: Target text for preview audio
			file_id: File ID of the uploaded audio file
			request_id: Optional request ID for tracking
			model: Model
			extra_headers: Additional headers to include in the request
			extra_body: Additional body parameters
			timeout: Request timeout

		Returns:
			Voice clone response
		"""
			
		return self._post(
			"/voice/clone",
			body=maybe_transform(
				{
					"voice_name": voice_name,
					"text": text,
					"input": input,
					"file_id": file_id,
					"request_id": request_id,
					"model": model,
				},
				VoiceCloneParams,
			),
			options=make_request_options(
				extra_headers=extra_headers,
				extra_body=extra_body,
				timeout=timeout,
			),
			cast_type=VoiceCloneResult,
			stream=False,
		)

	def delete(
		self,
		*,
		voice: str,
		request_id: Optional[str] = None,
		extra_headers: Headers | None = None,
		extra_body: Body | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> VoiceDeleteResult:
		"""
		Delete a cloned voice by voice ID
		
		Args:
			voice: The voice to delete
			request_id: Optional request ID for tracking
			extra_headers: Additional headers to include in the request
			extra_body: Additional body parameters
			timeout: Request timeout
			
		Returns:
			Voice deletion response
		"""
		return self._post(
			"/voice/delete",
			body=maybe_transform(
				{
					"voice": voice,
					"request_id": request_id,
				},
				VoiceDeleteParams,
			),
			options=make_request_options(
				extra_headers=extra_headers,
				extra_body=extra_body,
				timeout=timeout,
			),
			cast_type=VoiceDeleteResult,
			stream=False,
		)

	def list(
		self,
		*,
		voice_type: Optional[str] = None,
		voice_name: Optional[str] = None,
		request_id: Optional[str] = None,
		extra_headers: Headers | None = None,
		timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
	) -> VoiceListResult:
		"""
		List voices with optional filtering
		
		Args:
			voice_type: Type of voice to filter by
			voice_name: Name of voice to filter by
			request_id: Optional request ID for tracking
			extra_headers: Additional headers to include in the request
			timeout: Request timeout
			
		Returns:
			List of voices response
		"""
		return self._get(
			"/voice/list",
			options=make_request_options(
				extra_headers={
					**({} if request_id is None else {"Request-Id": request_id}),
					**(extra_headers or {}),
				},
				extra_query=maybe_transform(
					{
						"voiceType": voice_type,
						"voiceName": voice_name,
						"request_id": request_id,
					},
					VoiceListParams,
				),
				timeout=timeout,
			),
			cast_type=VoiceListResult,
		)