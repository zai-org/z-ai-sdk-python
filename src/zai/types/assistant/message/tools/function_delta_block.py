from typing import List, Union

from typing_extensions import Literal

__all__ = ['FunctionToolBlock']

from .....core import BaseModel


class FunctionToolOutput(BaseModel):
	"""
	Represents the output of a function tool.

	Attributes:
		content (str): The output content from the function
	"""

	content: str


class FunctionTool(BaseModel):
	"""
	Represents a function tool with its arguments and outputs.

	Attributes:
		name (str): Name of the function
		arguments (Union[str, dict]): Function arguments
		outputs (List[FunctionToolOutput]): List of function outputs
	"""

	name: str
	arguments: Union[str, dict]
	outputs: List[FunctionToolOutput]


class FunctionToolBlock(BaseModel):
	"""
	Represents a function tool block in assistant messages.

	Attributes:
		function (FunctionTool): The function tool instance
		type (Literal['function']): Type identifier, always 'function'
	"""

	function: FunctionTool
	type: Literal['function'] = 'drawing_tool'
