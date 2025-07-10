from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Dict, List, Union

from ...core import BaseAPI, deepcopy_minimal
from ...types.moderation.moderation_completion import Completion

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
	from ..._client import ZaiClient


class Moderations(BaseAPI):
	"""
	API resource for content moderation operations
	"""
	def __init__(self, client: ZaiClient) -> None:
		super().__init__(client)

	def create(
		self,
		*,
		model: str,
		input: Union[str, List[str], Dict],
	) -> Completion:
		"""
		Moderate content for safety and compliance
		
		Arguments:
			model (str): The moderation model to use
			input (Union[str, List[str], Dict]): Content to moderate
		"""
		body = deepcopy_minimal({'model': model, 'input': input})
		return self._post('/moderations', body=body, cast_type=Completion)
