from typing_extensions import Literal

from zai.core import BaseModel


class TextContentBlock(BaseModel):
	"""
	Represents a text content block in assistant messages.

	Attributes:
		content (str): The text content
		role (str): Role of the message sender, defaults to 'assistant'
		type (Literal['content']): Type identifier, always 'content'
	"""

	content: str
	role: str = 'assistant'
	type: Literal['content'] = 'content'
