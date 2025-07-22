from typing_extensions import Literal

from zai.core import BaseModel


class FileDeleted(BaseModel):
	id: str

	deleted: bool

	object: Literal['file']
