from typing import List

from typing_extensions import Literal

from .....core import BaseModel

__all__ = ['DrawingToolBlock']


class DrawingToolOutput(BaseModel):
	"""
	Represents the output of a drawing tool.

	Attributes:
		image (str): The generated image data or URL
	"""

	image: str


class DrawingTool(BaseModel):
	"""
	Represents a drawing tool with its input and outputs.

	Attributes:
		input (str): Input prompt or description for drawing
		outputs (List[DrawingToolOutput]): List of drawing outputs
	"""

	input: str
	outputs: List[DrawingToolOutput]


class DrawingToolBlock(BaseModel):
	"""
	Represents a drawing tool block in assistant messages.

	Attributes:
		drawing_tool (DrawingTool): The drawing tool instance
		type (Literal['drawing_tool']): Type identifier, always 'drawing_tool'
	"""

	drawing_tool: DrawingTool
	type: Literal['drawing_tool'] = 'drawing_tool'
