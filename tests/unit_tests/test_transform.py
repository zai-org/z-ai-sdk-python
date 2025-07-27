"""Tests for _transform module."""

import pytest
import io
import os
from pathlib import Path
from typing import Annotated, Dict, List, Optional, Union
from unittest.mock import Mock, patch

from zai.core._utils._transform import (
    PropertyInfo,
    PropertyFormat,
    is_base64_file_input,
    maybe_transform,
    transform,
    async_maybe_transform,
    async_transform,
)


class TestPropertyInfo:
    """Test PropertyInfo class."""

    def test_property_info_creation(self):
        """Test PropertyInfo creation with all parameters."""
        info = PropertyInfo(
            alias="test_alias",
            format="iso8601",
            format_template="template",
            discriminator="disc"
        )
        
        assert info.alias == "test_alias"
        assert info.format == "iso8601"
        assert info.format_template == "template"
        assert info.discriminator == "disc"

    def test_property_info_creation_with_none_values(self):
        """Test PropertyInfo creation with None values."""
        info = PropertyInfo()
        
        assert info.alias is None
        assert info.format is None
        assert info.format_template is None
        assert info.discriminator is None

    def test_property_info_repr(self):
        """Test PropertyInfo string representation."""
        info = PropertyInfo(
            alias="test_alias",
            format="base64",
            format_template="template",
            discriminator="disc"
        )
        
        repr_str = repr(info)
        assert "PropertyInfo" in repr_str
        assert "test_alias" in repr_str
        assert "base64" in repr_str
        assert "template" in repr_str
        assert "disc" in repr_str


class TestIsBase64FileInput:
    """Test is_base64_file_input function."""

    def test_is_base64_file_input_with_file_object(self):
        """Test is_base64_file_input with file object."""
        file_obj = io.StringIO("test content")
        assert is_base64_file_input(file_obj)

    def test_is_base64_file_input_with_pathlike(self):
        """Test is_base64_file_input with pathlike object."""
        path_obj = Path("test.txt")
        assert is_base64_file_input(path_obj)

    def test_is_base64_file_input_with_string(self):
        """Test is_base64_file_input with string."""
        assert not is_base64_file_input("test.txt")

    def test_is_base64_file_input_with_none(self):
        """Test is_base64_file_input with None."""
        assert not is_base64_file_input(None)

    def test_is_base64_file_input_with_int(self):
        """Test is_base64_file_input with integer."""
        assert not is_base64_file_input(42)


class TestTransform:
    """Test transform functions."""

    def test_maybe_transform_with_none(self):
        """Test maybe_transform with None input."""
        result = maybe_transform(None, str)
        assert result is None

    def test_maybe_transform_with_valid_data(self):
        """Test maybe_transform with valid data."""
        result = maybe_transform("test", str)
        assert result == "test"

    def test_transform_with_simple_type(self):
        """Test transform with simple type."""
        result = transform("test", str)
        assert result == "test"

    def test_transform_with_annotated_type(self):
        """Test transform with annotated type."""
        annotated_type = Annotated[str, PropertyInfo(alias="test_alias")]
        result = transform("test", annotated_type)
        assert result == "test"

    def test_transform_with_typeddict(self):
        """Test transform with TypedDict."""
        from typing import TypedDict
        
        class TestDict(TypedDict):
            name: str
            age: int
        
        data = {"name": "test", "age": 25}
        result = transform(data, TestDict)
        assert result == data

    def test_transform_with_list_type(self):
        """Test transform with list type."""
        data = ["a", "b", "c"]
        result = transform(data, List[str])
        assert result == data

    def test_transform_with_dict_type(self):
        """Test transform with dict type."""
        data = {"key": "value"}
        result = transform(data, Dict[str, str])
        assert result == data

    def test_transform_with_union_type(self):
        """Test transform with union type."""
        data = "test"
        result = transform(data, Union[str, int])
        assert result == data

    def test_transform_with_optional_type(self):
        """Test transform with optional type."""
        data = "test"
        result = transform(data, Optional[str])
        assert result == data

    def test_transform_with_none_optional(self):
        """Test transform with None for optional type."""
        result = transform(None, Optional[str])
        assert result is None

    def test_transform_with_annotated_list(self):
        """Test transform with annotated list."""
        annotated_type = Annotated[List[str], PropertyInfo(format="base64")]
        data = ["a", "b", "c"]
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_annotated_dict(self):
        """Test transform with annotated dict."""
        annotated_type = Annotated[Dict[str, str], PropertyInfo(alias="test_alias")]
        data = {"key": "value"}
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_format_iso8601(self):
        """Test transform with iso8601 format."""
        from datetime import datetime
        
        # 测试datetime对象转换为iso8601字符串
        annotated_type = Annotated[str, PropertyInfo(format="iso8601")]
        data = datetime(2023, 1, 1, 12, 0, 0)
        result = transform(data, annotated_type)
        assert result == "2023-01-01T12:00:00"

    def test_transform_with_format_base64(self):
        """Test transform with base64 format."""
        # 测试文件对象编码为base64
        from io import BytesIO
        
        annotated_type = Annotated[str, PropertyInfo(format="base64")]
        data = BytesIO(b"test")
        result = transform(data, annotated_type)
        assert result == "dGVzdA=="  # base64 encoded "test"

    def test_transform_with_format_custom(self):
        """Test transform with custom format."""
        from datetime import datetime
        
        # 测试datetime对象使用自定义格式
        annotated_type = Annotated[str, PropertyInfo(
            format="custom",
            format_template="%Y-%m-%d"
        )]
        data = datetime(2023, 1, 1, 12, 0, 0)
        result = transform(data, annotated_type)
        assert result == "2023-01-01"

    def test_transform_with_discriminator(self):
        """Test transform with discriminator."""
        annotated_type = Annotated[str, PropertyInfo(discriminator="type")]
        data = "test"
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_nested_annotated(self):
        """Test transform with nested annotated types."""
        inner_annotated = Annotated[str, PropertyInfo(alias="inner")]
        outer_annotated = Annotated[inner_annotated, PropertyInfo(alias="outer")]
        
        result = transform("test", outer_annotated)
        assert result == "test"

    def test_transform_with_complex_nested_structure(self):
        """Test transform with complex nested structure."""
        from typing import TypedDict
        
        class InnerDict(TypedDict):
            value: str
        
        class OuterDict(TypedDict):
            inner: InnerDict
            name: str
        
        data = {
            "inner": {"value": "test"},
            "name": "outer"
        }
        
        result = transform(data, OuterDict)
        assert result == data

    def test_transform_with_annotated_union(self):
        """Test transform with annotated union."""
        annotated_union = Annotated[Union[str, int], PropertyInfo(alias="union_field")]
        data = "test"
        result = transform(data, annotated_union)
        assert result == data

    def test_transform_with_annotated_optional(self):
        """Test transform with annotated optional."""
        annotated_optional = Annotated[Optional[str], PropertyInfo(alias="optional_field")]
        data = "test"
        result = transform(data, annotated_optional)
        assert result == data

    def test_transform_with_none_annotated_optional(self):
        """Test transform with None for annotated optional."""
        annotated_optional = Annotated[Optional[str], PropertyInfo(alias="optional_field")]
        result = transform(None, annotated_optional)
        assert result is None


class TestAsyncTransform:
    """Test async transform functions."""

    @pytest.mark.asyncio
    async def test_async_maybe_transform_with_none(self):
        """Test async_maybe_transform with None input."""
        result = await async_maybe_transform(None, str)
        assert result is None

    @pytest.mark.asyncio
    async def test_async_maybe_transform_with_valid_data(self):
        """Test async_maybe_transform with valid data."""
        result = await async_maybe_transform("test", str)
        assert result == "test"

    @pytest.mark.asyncio
    async def test_async_transform_with_simple_type(self):
        """Test async_transform with simple type."""
        result = await async_transform("test", str)
        assert result == "test"

    @pytest.mark.asyncio
    async def test_async_transform_with_annotated_type(self):
        """Test async_transform with annotated type."""
        annotated_type = Annotated[str, PropertyInfo(alias="test_alias")]
        result = await async_transform("test", annotated_type)
        assert result == "test"

    @pytest.mark.asyncio
    async def test_async_transform_with_typeddict(self):
        """Test async_transform with TypedDict."""
        from typing import TypedDict
        
        class TestDict(TypedDict):
            name: str
            age: int
        
        data = {"name": "test", "age": 25}
        result = await async_transform(data, TestDict)
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_list_type(self):
        """Test async_transform with list type."""
        data = ["a", "b", "c"]
        result = await async_transform(data, List[str])
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_dict_type(self):
        """Test async_transform with dict type."""
        data = {"key": "value"}
        result = await async_transform(data, Dict[str, str])
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_union_type(self):
        """Test async_transform with union type."""
        data = "test"
        result = await async_transform(data, Union[str, int])
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_optional_type(self):
        """Test async_transform with optional type."""
        data = "test"
        result = await async_transform(data, Optional[str])
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_none_optional(self):
        """Test async_transform with None for optional type."""
        result = await async_transform(None, Optional[str])
        assert result is None

    @pytest.mark.asyncio
    async def test_async_transform_with_format_iso8601(self):
        """Test async_transform with iso8601 format."""
        from datetime import datetime
        
        # 测试datetime对象转换为iso8601字符串
        annotated_type = Annotated[str, PropertyInfo(format="iso8601")]
        data = datetime(2023, 1, 1, 12, 0, 0)
        result = await async_transform(data, annotated_type)
        assert result == "2023-01-01T12:00:00"

    @pytest.mark.asyncio
    async def test_async_transform_with_format_base64(self):
        """Test async_transform with base64 format."""
        # 测试文件对象编码为base64
        from io import BytesIO
        
        annotated_type = Annotated[str, PropertyInfo(format="base64")]
        data = BytesIO(b"test")
        result = await async_transform(data, annotated_type)
        assert result == "dGVzdA=="  # base64 encoded "test"

    @pytest.mark.asyncio
    async def test_async_transform_with_format_custom(self):
        """Test async_transform with custom format."""
        from datetime import datetime
        
        # 测试datetime对象使用自定义格式
        annotated_type = Annotated[str, PropertyInfo(
            format="custom",
            format_template="%Y-%m-%d"
        )]
        data = datetime(2023, 1, 1, 12, 0, 0)
        result = await async_transform(data, annotated_type)
        assert result == "2023-01-01"

    @pytest.mark.asyncio
    async def test_async_transform_with_discriminator(self):
        """Test async_transform with discriminator."""
        annotated_type = Annotated[str, PropertyInfo(discriminator="type")]
        data = "test"
        result = await async_transform(data, annotated_type)
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_complex_nested_structure(self):
        """Test async_transform with complex nested structure."""
        from typing import TypedDict
        
        class InnerDict(TypedDict):
            value: str
        
        class OuterDict(TypedDict):
            inner: InnerDict
            name: str
        
        data = {
            "inner": {"value": "test"},
            "name": "outer"
        }
        
        result = await async_transform(data, OuterDict)
        assert result == data


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_transform_with_empty_list(self):
        """Test transform with empty list."""
        result = transform([], List[str])
        assert result == []

    def test_transform_with_empty_dict(self):
        """Test transform with empty dict."""
        result = transform({}, Dict[str, str])
        assert result == {}

    def test_transform_with_none_in_list(self):
        """Test transform with None in list."""
        data = ["a", None, "c"]
        result = transform(data, List[Optional[str]])
        assert result == data

    def test_transform_with_mixed_types_in_union(self):
        """Test transform with mixed types in union."""
        data = 42
        result = transform(data, Union[str, int])
        assert result == data

    def test_transform_with_invalid_format(self):
        """Test transform with invalid format."""
        annotated_type = Annotated[str, PropertyInfo(format="invalid_format")]
        data = "test"
        # Should handle invalid format gracefully
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_missing_format_template(self):
        """Test transform with missing format template for custom format."""
        annotated_type = Annotated[str, PropertyInfo(format="custom")]
        data = "test"
        # Should handle missing template gracefully
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_invalid_base64(self):
        """Test transform with invalid base64 data."""
        annotated_type = Annotated[str, PropertyInfo(format="base64")]
        data = "invalid_base64!"
        # Should handle invalid base64 gracefully
        result = transform(data, annotated_type)
        assert result == data

    def test_transform_with_invalid_iso8601(self):
        """Test transform with invalid iso8601 data."""
        from datetime import datetime
        
        annotated_type = Annotated[datetime, PropertyInfo(format="iso8601")]
        data = "invalid_datetime"
        # Should handle invalid datetime gracefully
        result = transform(data, annotated_type)
        assert result == data

    @pytest.mark.asyncio
    async def test_async_transform_with_empty_list(self):
        """Test async_transform with empty list."""
        result = await async_transform([], List[str])
        assert result == []

    @pytest.mark.asyncio
    async def test_async_transform_with_empty_dict(self):
        """Test async_transform with empty dict."""
        result = await async_transform({}, Dict[str, str])
        assert result == {}

    @pytest.mark.asyncio
    async def test_async_transform_with_invalid_format(self):
        """Test async_transform with invalid format."""
        annotated_type = Annotated[str, PropertyInfo(format="invalid_format")]
        data = "test"
        # Should handle invalid format gracefully
        result = await async_transform(data, annotated_type)
        assert result == data


class TestPropertyFormat:
    """Test PropertyFormat literal."""

    def test_property_format_values(self):
        """Test PropertyFormat literal values."""
        assert PropertyFormat.__args__ == ('iso8601', 'base64', 'custom')
        
        # Test that all values are valid
        assert 'iso8601' in PropertyFormat.__args__
        assert 'base64' in PropertyFormat.__args__
        assert 'custom' in PropertyFormat.__args__ 