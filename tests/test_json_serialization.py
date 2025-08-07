"""Test JSON serialization for BaseModel objects."""

import json
import pytest
from typing import Optional, List

from zai.core._base_models import BaseModel
from zai.core._json_encoder import ZAIJSONEncoder, json_dumps
from zai.core._http_client import HttpClient


class TestModel(BaseModel):
    """Test model for JSON serialization."""
    name: str
    age: Optional[int] = None
    tags: Optional[List[str]] = None


class TestMessage(BaseModel):
    """Test message model similar to CompletionMessage."""
    content: Optional[str] = None
    role: str
    tool_calls: Optional[List[dict]] = None


def test_base_model_dict_conversion():
    """Test that BaseModel can be converted to dict."""
    model = TestModel(name="test", age=25, tags=["tag1", "tag2"])
    
    # Test model_dump() method
    model_dict = model.model_dump()
    assert model_dict == {"name": "test", "age": 25, "tags": ["tag1", "tag2"]}
    
    # Test keys/values/items methods
    assert list(model.keys()) == ["name", "age", "tags"]
    assert list(model.values()) == ["test", 25, ["tag1", "tag2"]]
    assert list(model.items()) == [("name", "test"), ("age", 25), ("tags", ["tag1", "tag2"])]


def test_zai_json_encoder():
    """Test custom JSON encoder for BaseModel objects."""
    model = TestModel(name="test", age=25)
    
    # Test with custom encoder
    json_str = json.dumps(model, cls=ZAIJSONEncoder)
    result = json.loads(json_str)
    assert result == {"name": "test", "age": 25}
    
    # Test with nested BaseModel
    message = TestMessage(content="hello", role="user")
    nested_data = {"message": message, "other": "data"}
    
    json_str = json.dumps(nested_data, cls=ZAIJSONEncoder)
    result = json.loads(json_str)
    assert result == {
        "message": {"content": "hello", "role": "user"},
        "other": "data"
    }


def test_json_dumps_utility():
    """Test the json_dumps utility function."""
    model = TestModel(name="test", age=25)
    
    json_str = json_dumps(model)
    result = json.loads(json_str)
    assert result == {"name": "test", "age": 25}


def test_http_client_json_preparation():
    """Test that HttpClient can prepare JSON data with BaseModel objects."""
    # We'll create a minimal HttpClient to test the _prepare_json_data method
    import httpx
    from zai.core._http_client import HttpClient
    
    # Create a minimal client for testing
    client = HttpClient(
        base_url="https://test.com",
        api_key="test_key",
        httpx_client=httpx.Client()
    )
    
    # Test with BaseModel
    model = TestModel(name="test", age=25)
    result = client._prepare_json_data(model)
    assert result == {"name": "test", "age": 25}
    
    # Test with list containing BaseModel
    models = [TestModel(name="test1", age=25), TestModel(name="test2", age=30)]
    result = client._prepare_json_data(models)
    expected = [
        {"name": "test1", "age": 25},
        {"name": "test2", "age": 30}
    ]
    assert result == expected
    
    # Test with dict containing BaseModel
    data = {
        "message": TestMessage(content="hello", role="user"),
        "count": 1
    }
    result = client._prepare_json_data(data)
    expected = {
        "message": {"content": "hello", "role": "user"},
        "count": 1
    }
    assert result == expected
    
    # Test with None
    assert client._prepare_json_data(None) is None
    
    # Test with regular data
    regular_data = {"key": "value", "number": 42}
    assert client._prepare_json_data(regular_data) == regular_data


def test_completion_message_like_serialization():
    """Test serialization for CompletionMessage-like objects."""
    # Simulate a CompletionMessage-like object
    message = TestMessage(
        content="Hello, how can I help you?",
        role="assistant",
        tool_calls=[{"id": "call_123", "function": {"name": "test_func"}}]
    )
    
    # Test that it can be serialized
    json_str = json_dumps(message)
    result = json.loads(json_str)
    
    expected = {
        "content": "Hello, how can I help you?",
        "role": "assistant",
        "tool_calls": [{"id": "call_123", "function": {"name": "test_func"}}]
    }
    assert result == expected
    
    # Test in a messages list (similar to the original error case)
    messages = [
        {"role": "user", "content": "Help me"},
        message  # This is a BaseModel object
    ]
    
    # This should work now with our custom encoder
    json_str = json_dumps(messages)
    result = json.loads(json_str)
    
    expected = [
        {"role": "user", "content": "Help me"},
        {
            "content": "Hello, how can I help you?",
            "role": "assistant",
            "tool_calls": [{"id": "call_123", "function": {"name": "test_func"}}]
        }
    ]
    assert result == expected


if __name__ == "__main__":
    # Run basic tests
    test_base_model_dict_conversion()
    test_zai_json_encoder()
    test_json_dumps_utility()
    test_http_client_json_preparation()
    test_completion_message_like_serialization()
    print("All tests passed!")
