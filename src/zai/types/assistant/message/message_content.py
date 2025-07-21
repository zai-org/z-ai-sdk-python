from typing import Union

from typing_extensions import Annotated, TypeAlias

from zai.core._utils import PropertyInfo
from zai.types.assistant.message.text_content_block import TextContentBlock
from zai.types.assistant.message.tools_delta_block import ToolsDeltaBlock

MessageContent: TypeAlias = Annotated[
	Union[ToolsDeltaBlock, TextContentBlock],
	PropertyInfo(discriminator='type'),
]
