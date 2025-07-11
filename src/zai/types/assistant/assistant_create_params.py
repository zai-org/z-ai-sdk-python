from typing import List, Optional, TypedDict, Union


class AssistantAttachments:
	"""
	Assistant conversation file attachments

	Attributes:
		file_id (str): File identifier for attachment
	"""

	file_id: str


class MessageTextContent:
	"""
	Text content for conversation messages

	Attributes:
		type (str): Content type, currently supports 'text'
		text (str): Text content of the message
	"""

	type: str
	text: str


MessageContent = Union[MessageTextContent]


class ConversationMessage(TypedDict):
	"""
	Conversation message structure

	Attributes:
		role (str): Message role (e.g., 'user', 'assistant')
		content (List[MessageContent]): List of message content items
	"""

	role: str
	content: List[MessageContent]


class AssistantParameters(TypedDict, total=False):
	"""
	Assistant conversation parameters

	Attributes:
		assistant_id (str): Assistant identifier
		conversation_id (Optional[str]): Conversation ID, creates new conversation if not provided
		model (str): Model name, default is 'GLM-4-Assistant'
		stream (bool): Whether to enable streaming SSE responses
		messages (List[ConversationMessage]): List of conversation messages
		attachments (Optional[List[AssistantAttachments]]): Optional file attachments for conversation
		metadata (Optional[dict]): Optional metadata extension field
	"""

	assistant_id: str
	conversation_id: Optional[str]
	model: str
	stream: bool
	messages: List[ConversationMessage]
	attachments: Optional[List[AssistantAttachments]]
	metadata: Optional[dict]


class TranslateParameters(TypedDict, total=False):
	"""
	Translation parameters

	Attributes:
		from_language (str): Source language code
		to_language (str): Target language code
	"""

	from_language: str
	to_language: str


class ExtraParameters(TypedDict, total=False):
	"""
	Extra parameters for assistant functionality

	Attributes:
		translate (TranslateParameters): Translation configuration parameters
	"""

	translate: TranslateParameters
