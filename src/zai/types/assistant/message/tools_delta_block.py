from typing import List

from typing_extensions import Literal

from ....core import BaseModel
from .tools.tools_type import ToolsType

__all__ = ['ToolsDeltaBlock']


class ToolsDeltaBlock(BaseModel):
	"""
	Represents a tools delta block in assistant messages.

	Attributes:
		tool_calls (List[ToolsType]): List of tool calls, The index of the content part in the message.
		role (str): Role of the message sender, defaults to 'tool'
		type (Literal['tool_calls']): Type identifier, always 'tool_calls'
	"""

	tool_calls: List[ToolsType]
	role: str = 'tool'
	type: Literal['tool_calls'] = 'tool_calls'
