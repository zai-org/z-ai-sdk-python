"""Tests for _utils module."""

import pytest
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from unittest.mock import Mock, patch

from zai.core._utils._utils import (
    remove_notgiven_indict,
    flatten,
    extract_files,
    is_given,
    is_tuple,
    is_tuple_t,
    is_sequence,
    is_sequence_t,
    is_mapping,
    is_mapping_t,
    is_dict,
    is_list,
    is_iterable,
    deepcopy_minimal,
    human_join,
    quote,
    required_args,
    strip_not_given,
    coerce_integer,
    coerce_float,
    coerce_boolean,
    maybe_coerce_integer,
    maybe_coerce_float,
    maybe_coerce_boolean,
    removeprefix,
    removesuffix,
    file_from_path,
    get_required_header,
    get_async_library,
    drop_prefix_image_data,
)
from zai.core._base_type import NOT_GIVEN


class TestRemoveNotGivenInDict:
    """Test remove_notgiven_indict function."""

    def test_remove_notgiven_indict_with_none(self):
        """Test remove_notgiven_indict with None."""
        result = remove_notgiven_indict(None)
        assert result is None

    def test_remove_notgiven_indict_with_non_dict(self):
        """Test remove_notgiven_indict with non-dict."""
        result = remove_notgiven_indict("not_a_dict")
        assert result == "not_a_dict"

    def test_remove_notgiven_indict_with_dict_no_notgiven(self):
        """Test remove_notgiven_indict with dict containing no NotGiven values."""
        data = {"key1": "value1", "key2": "value2"}
        result = remove_notgiven_indict(data)
        assert result == data

    def test_remove_notgiven_indict_with_dict_with_notgiven(self):
        """Test remove_notgiven_indict with dict containing NotGiven values."""
        data = {"key1": "value1", "key2": NOT_GIVEN, "key3": "value3"}
        result = remove_notgiven_indict(data)
        assert result == {"key1": "value1", "key3": "value3"}

    def test_remove_notgiven_indict_with_nested_dict(self):
        """Test remove_notgiven_indict with nested dict."""
        data = {
            "key1": "value1",
            "nested": {"key2": NOT_GIVEN, "key3": "value3"}
        }
        result = remove_notgiven_indict(data)
        # Should not modify nested dicts
        assert result == data


class TestFlatten:
    """Test flatten function."""

    def test_flatten_empty_list(self):
        """Test flatten with empty list."""
        result = flatten([])
        assert result == []

    def test_flatten_single_level(self):
        """Test flatten with single level list."""
        data = [[1, 2], [3, 4], [5, 6]]
        result = flatten(data)
        assert result == [1, 2, 3, 4, 5, 6]

    def test_flatten_mixed_types(self):
        """Test flatten with mixed types."""
        data = [["a", "b"], [1, 2], ["c"]]
        result = flatten(data)
        assert result == ["a", "b", 1, 2, "c"]

    def test_flatten_empty_inner_lists(self):
        """Test flatten with empty inner lists."""
        data = [[], [1, 2], [], [3, 4]]
        result = flatten(data)
        assert result == [1, 2, 3, 4]


class TestExtractFiles:
    """Test extract_files function."""

    def test_extract_files_empty_paths(self):
        """Test extract_files with empty paths."""
        query = {"key": "value"}
        result = extract_files(query, paths=[])
        assert result == []

    def test_extract_files_simple_path(self):
        """Test extract_files with simple path."""
        from io import BytesIO
        query = {"file": BytesIO(b"file_content")}
        result = extract_files(query, paths=[["file"]])
        assert len(result) == 1
        assert result[0][0] == "file"
        assert isinstance(result[0][1], BytesIO)  # 返回BytesIO对象

    def test_extract_files_nested_path(self):
        """Test extract_files with nested path."""
        from io import BytesIO
        query = {"nested": {"file": BytesIO(b"file_content")}}
        result = extract_files(query, paths=[["nested", "file"]])
        assert len(result) == 1
        assert result[0][0] == "nested[file]"
        assert isinstance(result[0][1], BytesIO)  # 返回BytesIO对象

    def test_extract_files_array_path(self):
        """Test extract_files with array path."""
        from io import BytesIO
        query = {"files": [{"data": BytesIO(b"file1")}, {"data": BytesIO(b"file2")}]}
        result = extract_files(query, paths=[["files", "<array>", "data"]])
        assert len(result) == 2
        assert result[0][0] == "files[][data]"
        assert isinstance(result[0][1], BytesIO)  # 返回BytesIO对象
        assert result[1][0] == "files[][data]"
        assert isinstance(result[1][1], BytesIO)  # 返回BytesIO对象

    def test_extract_files_multiple_paths(self):
        """Test extract_files with multiple paths."""
        from io import BytesIO
        query = {
            "file1": BytesIO(b"content1"),
            "nested": {"file2": BytesIO(b"content2")}
        }
        result = extract_files(query, paths=[["file1"], ["nested", "file2"]])
        assert len(result) == 2
        assert result[0][0] == "file1"
        assert isinstance(result[0][1], BytesIO)  # 返回BytesIO对象
        assert result[1][0] == "nested[file2]"
        assert isinstance(result[1][1], BytesIO)  # 返回BytesIO对象

    def test_extract_files_missing_key(self):
        """Test extract_files with missing key."""
        query = {"key": "value"}
        result = extract_files(query, paths=[["missing_key"]])
        assert result == []

    def test_extract_files_with_notgiven(self):
        """Test extract_files with NotGiven value."""
        query = {"file": NOT_GIVEN}
        result = extract_files(query, paths=[["file"]])
        assert result == []


class TestTypeGuards:
    """Test type guard functions."""

    def test_is_given(self):
        """Test is_given function."""
        assert is_given("value") is True
        assert is_given(42) is True
        assert is_given(NOT_GIVEN) is False

    def test_is_tuple(self):
        """Test is_tuple function."""
        assert is_tuple((1, 2, 3)) is True
        assert is_tuple([1, 2, 3]) is False
        assert is_tuple("string") is False

    def test_is_tuple_t(self):
        """Test is_tuple_t function."""
        tuple_data = (1, 2, 3)
        assert is_tuple_t(tuple_data) is True
        assert is_tuple_t([1, 2, 3]) is False

    def test_is_sequence(self):
        """Test is_sequence function."""
        assert is_sequence([1, 2, 3]) is True
        assert is_sequence((1, 2, 3)) is True
        assert is_sequence("string") is True
        assert is_sequence(42) is False

    def test_is_sequence_t(self):
        """Test is_sequence_t function."""
        list_data = [1, 2, 3]
        assert is_sequence_t(list_data) is True
        assert is_sequence_t(42) is False

    def test_is_mapping(self):
        """Test is_mapping function."""
        assert is_mapping({"key": "value"}) is True
        assert is_mapping([1, 2, 3]) is False
        assert is_mapping("string") is False

    def test_is_mapping_t(self):
        """Test is_mapping_t function."""
        dict_data = {"key": "value"}
        assert is_mapping_t(dict_data) is True
        assert is_mapping_t([1, 2, 3]) is False

    def test_is_dict(self):
        """Test is_dict function."""
        assert is_dict({"key": "value"}) is True
        assert is_dict([1, 2, 3]) is False
        assert is_dict("string") is False

    def test_is_list(self):
        """Test is_list function."""
        assert is_list([1, 2, 3]) is True
        assert is_list((1, 2, 3)) is False
        assert is_list("string") is False

    def test_is_iterable(self):
        """Test is_iterable function."""
        assert is_iterable([1, 2, 3]) is True
        assert is_iterable((1, 2, 3)) is True
        assert is_iterable("string") is True
        assert is_iterable(42) is False


class TestDeepcopyMinimal:
    """Test deepcopy_minimal function."""

    def test_deepcopy_minimal_with_primitive(self):
        """Test deepcopy_minimal with primitive types."""
        assert deepcopy_minimal("string") == "string"
        assert deepcopy_minimal(42) == 42
        assert deepcopy_minimal(True) is True

    def test_deepcopy_minimal_with_list(self):
        """Test deepcopy_minimal with list."""
        original = [1, 2, 3]
        copied = deepcopy_minimal(original)
        assert copied == original
        assert copied is not original

    def test_deepcopy_minimal_with_dict(self):
        """Test deepcopy_minimal with dict."""
        original = {"key": "value"}
        copied = deepcopy_minimal(original)
        assert copied == original
        assert copied is not original

    def test_deepcopy_minimal_with_nested_structure(self):
        """Test deepcopy_minimal with nested structure."""
        original = {"list": [1, 2, 3], "dict": {"nested": "value"}}
        copied = deepcopy_minimal(original)
        assert copied == original
        assert copied is not original
        assert copied["list"] is not original["list"]
        assert copied["dict"] is not original["dict"]


class TestHumanJoin:
    """Test human_join function."""

    def test_human_join_empty_sequence(self):
        """Test human_join with empty sequence."""
        result = human_join([])
        assert result == ""

    def test_human_join_single_item(self):
        """Test human_join with single item."""
        result = human_join(["apple"])
        assert result == "apple"

    def test_human_join_two_items(self):
        """Test human_join with two items."""
        result = human_join(["apple", "banana"])
        assert result == "apple or banana"

    def test_human_join_multiple_items(self):
        """Test human_join with multiple items."""
        result = human_join(["apple", "banana", "cherry"])
        assert result == "apple, banana or cherry"

    def test_human_join_custom_delimiter(self):
        """Test human_join with custom delimiter."""
        result = human_join(["apple", "banana", "cherry"], delim="; ")
        assert result == "apple; banana or cherry"

    def test_human_join_custom_final(self):
        """Test human_join with custom final."""
        result = human_join(["apple", "banana", "cherry"], final="and")
        assert result == "apple, banana and cherry"


class TestQuote:
    """Test quote function."""

    def test_quote_simple_string(self):
        """Test quote with simple string."""
        result = quote("hello")
        assert result == "'hello'"

    def test_quote_empty_string(self):
        """Test quote with empty string."""
        result = quote("")
        assert result == "''"

    def test_quote_string_with_quotes(self):
        """Test quote with string containing quotes."""
        result = quote('hello "world"')
        assert result == "'hello \"world\"'"


class TestRequiredArgs:
    """Test required_args decorator."""

    def test_required_args_single_variant(self):
        """Test required_args with single variant."""
        @required_args(["name"])
        def test_func(name, age=None):
            return f"{name}: {age}"
        
        result = test_func("John", age=25)
        assert result == "John: 25"

    def test_required_args_multiple_variants(self):
        """Test required_args with multiple variants."""
        @required_args(["name"], ["age"])
        def test_func(name, age, city=None):
            return f"{name}: {age} from {city}"

        result = test_func("John", 25, city="NYC")
        assert result == "John: 25 from NYC"

    def test_required_args_missing_required(self):
        """Test required_args with missing required argument."""
        @required_args(["name"])
        def test_func(name, age=None):
            return f"{name}: {age}"

        with pytest.raises(TypeError):
            test_func(age=25)  # Missing name


class TestStripNotGiven:
    """Test strip_not_given function."""

    def test_strip_not_given_with_none(self):
        """Test strip_not_given with None."""
        result = strip_not_given(None)
        assert result is None

    def test_strip_not_given_with_notgiven(self):
        """Test strip_not_given with NotGiven."""
        result = strip_not_given(NOT_GIVEN)
        # strip_not_given只处理Mapping类型，其他类型直接返回
        assert result == NOT_GIVEN

    def test_strip_not_given_with_other_value(self):
        """Test strip_not_given with other value."""
        result = strip_not_given("value")
        assert result == "value"

    def test_strip_not_given_with_dict(self):
        """Test strip_not_given with dict."""
        data = {"key1": "value1", "key2": NOT_GIVEN, "key3": "value3"}
        result = strip_not_given(data)
        assert result == {"key1": "value1", "key3": "value3"}

    def test_strip_not_given_with_list(self):
        """Test strip_not_given with list."""
        data = ["value1", NOT_GIVEN, "value3"]
        result = strip_not_given(data)
        # strip_not_given只处理Mapping类型，列表直接返回
        assert result == data


class TestCoerceFunctions:
    """Test coercion functions."""

    def test_coerce_integer(self):
        """Test coerce_integer function."""
        assert coerce_integer("42") == 42
        assert coerce_integer("-123") == -123

    def test_coerce_float(self):
        """Test coerce_float function."""
        assert coerce_float("42.5") == 42.5
        assert coerce_float("-123.0") == -123.0

    def test_coerce_boolean(self):
        """Test coerce_boolean function."""
        assert coerce_boolean("true") is True
        assert coerce_boolean("false") is False
        assert coerce_boolean("1") is True
        assert coerce_boolean("on") is True
        assert coerce_boolean("True") is False  # 只接受小写
        assert coerce_boolean("False") is False

    def test_maybe_coerce_integer(self):
        """Test maybe_coerce_integer function."""
        assert maybe_coerce_integer("42") == 42
        assert maybe_coerce_integer(None) is None

    def test_maybe_coerce_float(self):
        """Test maybe_coerce_float function."""
        assert maybe_coerce_float("42.5") == 42.5
        assert maybe_coerce_float(None) is None

    def test_maybe_coerce_boolean(self):
        """Test maybe_coerce_boolean function."""
        assert maybe_coerce_boolean("true") is True
        assert maybe_coerce_boolean(None) is None


class TestStringFunctions:
    """Test string utility functions."""

    def test_removeprefix(self):
        """Test removeprefix function."""
        assert removeprefix("hello world", "hello ") == "world"
        assert removeprefix("hello world", "goodbye ") == "hello world"
        assert removeprefix("hello", "hello") == ""

    def test_removesuffix(self):
        """Test removesuffix function."""
        assert removesuffix("hello world", " world") == "hello"
        assert removesuffix("hello world", " goodbye") == "hello world"
        assert removesuffix("hello", "hello") == ""


class TestFileFromPath:
    """Test file_from_path function."""

    def test_file_from_path_with_existing_file(self):
        """Test file_from_path with existing file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_path = f.name

        try:
            result = file_from_path(temp_path)
            assert result is not None
        finally:
            os.unlink(temp_path)

    def test_file_from_path_with_nonexistent_file(self):
        """Test file_from_path with nonexistent file."""
        with pytest.raises(FileNotFoundError):
            file_from_path("nonexistent_file.txt")


class TestGetRequiredHeader:
    """Test get_required_header function."""

    def test_get_required_header_with_dict(self):
        """Test get_required_header with dict."""
        headers = {"content-type": "application/json", "authorization": "Bearer token"}
        result = get_required_header(headers, "content-type")
        assert result == "application/json"

    def test_get_required_header_with_list(self):
        """Test get_required_header with list."""
        headers = [("content-type", "application/json"), ("authorization", "Bearer token")]
        with pytest.raises(AttributeError):
            get_required_header(headers, "content-type")

    def test_get_required_header_missing_header(self):
        """Test get_required_header with missing header."""
        headers = {"content-type": "application/json"}
        with pytest.raises(ValueError):
            get_required_header(headers, "authorization")

    def test_get_required_header_case_insensitive(self):
        """Test get_required_header case insensitive."""
        headers = {"Content-Type": "application/json"}
        result = get_required_header(headers, "content-type")
        assert result == "application/json"


class TestGetAsyncLibrary:
    """Test get_async_library function."""

    def test_get_async_library(self):
        """Test get_async_library function."""
        result = get_async_library()
        # 在测试环境中可能返回'false'，这是正常的
        assert result in ["asyncio", "trio", "false"]


class TestDropPrefixImageData:
    """Test drop_prefix_image_data function."""

    def test_drop_prefix_image_data_with_string(self):
        """Test drop_prefix_image_data with string."""
        data = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
        result = drop_prefix_image_data(data)
        # 字符串不会被处理，直接返回
        assert result == data

    def test_drop_prefix_image_data_without_prefix(self):
        """Test drop_prefix_image_data without prefix."""
        data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
        result = drop_prefix_image_data(data)
        assert result == data

    def test_drop_prefix_image_data_with_list(self):
        """Test drop_prefix_image_data with list."""
        data = [
            {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="}},
            {"type": "text", "text": "Hello"}
        ]
        result = drop_prefix_image_data(data)
        assert len(result) == 2
        assert result[0]["image_url"]["url"] == "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
        assert result[1]["text"] == "Hello"

    def test_drop_prefix_image_data_with_empty_list(self):
        """Test drop_prefix_image_data with empty list."""
        result = drop_prefix_image_data([])
        assert result == []

    def test_drop_prefix_image_data_with_none(self):
        """Test drop_prefix_image_data with None."""
        result = drop_prefix_image_data(None)
        assert result is None


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_extract_files_with_invalid_path(self):
        """Test extract_files with invalid path."""
        query = {"key": "value"}
        result = extract_files(query, paths=[["key", "nonexistent"]])
        assert result == []

    def test_extract_files_with_empty_array(self):
        """Test extract_files with empty array."""
        query = {"files": []}
        result = extract_files(query, paths=[["files", "<array>", "data"]])
        assert result == []

    def test_coerce_integer_invalid_input(self):
        """Test coerce_integer with invalid input."""
        with pytest.raises(ValueError):
            coerce_integer("not_a_number")

    def test_coerce_float_invalid_input(self):
        """Test coerce_float with invalid input."""
        with pytest.raises(ValueError):
            coerce_float("not_a_number")

    def test_coerce_boolean_invalid_input(self):
        """Test coerce_boolean with invalid input."""
        # coerce_boolean不会抛出ValueError，只会返回False
        assert coerce_boolean("invalid") is False

    def test_get_required_header_with_empty_headers(self):
        """Test get_required_header with empty headers."""
        with pytest.raises(ValueError):
            get_required_header({}, "content-type")

    def test_get_required_header_with_none_headers(self):
        """Test get_required_header with None headers."""
        with pytest.raises(AttributeError):
            get_required_header(None, "content-type") 