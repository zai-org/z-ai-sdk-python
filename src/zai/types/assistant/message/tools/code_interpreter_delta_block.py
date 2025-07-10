from typing import List

from typing_extensions import Literal

__all__ = ['CodeInterpreterToolBlock']

from .....core import BaseModel


class CodeInterpreterToolOutput(BaseModel):
	"""Code tool output result"""

	type: str  # Code execution log, currently only logs
	logs: str  # Code execution log result
	error_msg: str  # Error message


class CodeInterpreter(BaseModel):
	"""Code interpreter"""

	input: str  # Generated code snippet, input to code sandbox
	outputs: List[CodeInterpreterToolOutput]  # Output result after code execution


class CodeInterpreterToolBlock(BaseModel):
	"""Code tool block"""

	code_interpreter: CodeInterpreter  # Code interpreter object
	type: Literal['code_interpreter']  # Type of tool called, always `code_interpreter`
