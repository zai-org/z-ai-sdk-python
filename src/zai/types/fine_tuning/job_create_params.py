from __future__ import annotations

from typing import Union

from typing_extensions import Literal, TypedDict

__all__ = ['Hyperparameters']


class Hyperparameters(TypedDict, total=False):
	"""
	Hyperparameters for fine-tuning job configuration
	
	Attributes:
		batch_size: The batch size to use for training (can be 'auto' or an integer)
		learning_rate_multiplier: The learning rate multiplier for training (can be 'auto' or a float)
		n_epochs: The number of epochs to train for (can be 'auto' or an integer)
	"""
	batch_size: Union[Literal['auto'], int]
	learning_rate_multiplier: Union[Literal['auto'], float]
	n_epochs: Union[Literal['auto'], int]
