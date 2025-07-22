from typing import ClassVar

from zai.core import PYDANTIC_V2, BaseModel, ConfigDict


class FineTunedModelsStatus(BaseModel):
	"""
	Fine-tuned model status

	Attributes:
		request_id (str): Request id
		model_name (str): Model name
		delete_status (str): Delete status: deleting (deleting), deleted (deleted)
	"""

	if PYDANTIC_V2:
		model_config: ClassVar[ConfigDict] = ConfigDict(extra='allow', protected_namespaces=())
	request_id: str
	model_name: str
	delete_status: str
