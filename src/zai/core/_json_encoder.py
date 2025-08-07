"""JSON encoding utilities for BaseModel objects."""

import json
from typing import Any

from ._base_models import BaseModel


class ZAIJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles BaseModel objects."""
    
    def default(self, obj: Any) -> Any:
        """Override default method to handle BaseModel objects."""
        if isinstance(obj, BaseModel):
            return obj.model_dump(by_alias=True, exclude_unset=True)
        return super().default(obj)


def json_dumps(obj: Any, **kwargs) -> str:
    """
    JSON dumps with support for BaseModel objects.
    
    Args:
        obj: Object to serialize
        **kwargs: Additional arguments to pass to json.dumps()
        
    Returns:
        JSON string representation
    """
    return json.dumps(obj, cls=ZAIJSONEncoder, **kwargs)


def json_loads(s: str, **kwargs) -> Any:
    """
    JSON loads with consistent interface.
    
    Args:
        s: JSON string to deserialize
        **kwargs: Additional arguments to pass to json.loads()
        
    Returns:
        Deserialized object
    """
    return json.loads(s, **kwargs)
