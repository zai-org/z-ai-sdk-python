from ..core import BaseModel

__all__ = ['BatchRequestCounts']


class BatchRequestCounts(BaseModel):
	completed: int
	"""The number of requests that have been completed."""

	failed: int
	"""The number of failed requests."""

	total: int
	"""The total number of requests."""
