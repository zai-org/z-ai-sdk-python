from typing import Optional

from ...core import BaseModel

__all__ = ['KnowledgeInfo']


class KnowledgeInfo(BaseModel):
	# Knowledge base unique ID
	id: Optional[str] = None

	# Vectorization model bound to knowledge base
	# See model list [Internal Service Open Interface Documentation](https://lslfd0slxc.feishu.cn/docx/YauWdbBiMopV0FxB7KncPWCEn8f#H15NduiQZo3ugmxnWQFcfAHpnQ4)
	embedding_id: Optional[str] = None

	# Knowledge base name, 100 character limit
	name: Optional[str] = None

	# User identifier, within 32 characters
	customer_identifier: Optional[str] = None

	# Knowledge base description, 500 character limit
	description: Optional[str] = None

	# Background color (enumeration) 'blue', 'red', 'orange', 'purple', 'sky'
	background: Optional[str] = None

	# Knowledge base icon (enumeration) question: question mark, book: book, seal: seal, wrench: wrench,
	# tag: tag, horn: horn, house: house
	icon: Optional[str] = None

	# Bucket ID, 32 character limit
	bucket_id: Optional[str] = None
