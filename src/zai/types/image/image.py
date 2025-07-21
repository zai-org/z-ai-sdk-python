from __future__ import annotations

from typing import List, Optional

from ..core import BaseModel

__all__ = ['GeneratedImage', 'ImagesResponded']


class GeneratedImage(BaseModel):
	"""
	Generated image data

	Attributes:
		b64_json (Optional[str]): Base64 encoded image data
		url (Optional[str]): URL of the generated image
		revised_prompt (Optional[str]): Revised prompt used for generation
	"""

	b64_json: Optional[str] = None
	url: Optional[str] = None
	revised_prompt: Optional[str] = None


class ImagesResponded(BaseModel):
	"""
	Image generation response

	Attributes:
		created (int): Creation timestamp
		data (List[GeneratedImage]): List of generated images
	"""

	created: int
	data: List[GeneratedImage]
