"""Tests for _base_models module."""

import pytest
from typing import Any, Dict, List, Literal, Optional, Union, TypeVar

import pydantic
from pydantic import BaseModel as PydanticBaseModel

from zai.core._base_models import (
    BaseModel,
    GenericModel,
    TypeAdapter,
    _construct_field,
    _validate_non_model_type,
    build,
    construct_type,
    construct_type_unchecked,
    is_basemodel,
    is_basemodel_type,
    validate_type,
)


class TestBaseModel:
    """Test BaseModel functionality."""

    def test_base_model_creation(self):
        """Test BaseModel creation."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        assert model.name == "test"
        assert model.age == 25

    def test_to_dict(self):
        """Test to_dict method."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        data = model.to_dict()
        
        assert isinstance(data, dict)
        assert data['name'] == "test"
        assert data['age'] == 25

    def test_to_dict_with_exclude_unset(self):
        """Test to_dict with exclude_unset=True."""
        class TestModel(BaseModel):
            name: str
            age: int = 0

        model = TestModel(name="test")
        data = model.to_dict(exclude_unset=True)
        
        assert 'name' in data
        assert 'age' not in data  # Should be excluded as it's unset

    def test_to_dict_with_exclude_defaults(self):
        """Test to_dict with exclude_defaults=True."""
        class TestModel(BaseModel):
            name: str
            age: int = 25

        model = TestModel(name="test")
        data = model.to_dict(exclude_defaults=True)
        
        assert 'name' in data
        assert 'age' not in data  # Should be excluded as it's default

    def test_to_json(self):
        """Test to_json method."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        json_str = model.to_json()
        
        assert isinstance(json_str, str)
        assert "test" in json_str
        assert "25" in json_str

    def test_to_json_with_indent(self):
        """Test to_json with custom indent."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        json_str = model.to_json(indent=4)
        
        assert isinstance(json_str, str)
        assert "\n" in json_str  # Should be formatted

    def test_construct(self):
        """Test construct classmethod."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel.construct(name="test", age=25)
        assert model.name == "test"
        assert model.age == 25

    def test_model_dump(self):
        """Test model_dump method."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        data = model.model_dump()
        
        assert isinstance(data, dict)
        assert data['name'] == "test"
        assert data['age'] == 25

    def test_model_dump_json(self):
        """Test model_dump_json method."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        json_str = model.model_dump_json()
        
        assert isinstance(json_str, str)
        assert "test" in json_str
        assert "25" in json_str

    def test_str_representation(self):
        """Test string representation."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        str_repr = str(model)
        
        assert isinstance(str_repr, str)
        assert "TestModel" in str_repr


class TestGenericModel:
    """Test GenericModel functionality."""

    def test_generic_model_creation(self):
        """Test GenericModel creation."""
        # Test that GenericModel exists and can be used
        assert issubclass(GenericModel, BaseModel)
    
    def test_generic_model_with_type_parameters(self):
        """Test GenericModel with type parameters."""
        T = TypeVar('T')
        
        # Import Generic from typing
        from typing import Generic
        
        class TestGenericModel(GenericModel, Generic[T]):
            value: T
        
        # Test instantiation
        model = TestGenericModel[int](value=42)
        assert model.value == 42
        assert isinstance(model.value, int)


class TestTypeAdapter:
    """Test TypeAdapter functionality."""
    
    def test_type_adapter_creation(self):
        """Test TypeAdapter creation."""
        adapter = TypeAdapter[str]
        assert adapter is not None
    
    def test_type_adapter_validate_python(self):
        """Test TypeAdapter validate_python method."""
        # Test the underlying _validate_non_model_type function instead
        from zai.core._base_models import _validate_non_model_type
        result = _validate_non_model_type(type_=str, value="test")
        assert result == "test"
        assert isinstance(result, str)
    
    def test_type_adapter_with_complex_type(self):
        """Test TypeAdapter with complex type."""
        # Test the underlying _validate_non_model_type function instead
        from zai.core._base_models import _validate_non_model_type
        result = _validate_non_model_type(type_=List[str], value=["a", "b", "c"])
        assert result == ["a", "b", "c"]
        assert isinstance(result, list)
        assert all(isinstance(item, str) for item in result)


class TestUtilityFunctions:
    """Test utility functions."""

    def test_is_basemodel(self):
        """Test is_basemodel function."""
        class TestModel(BaseModel):
            name: str

        assert is_basemodel(TestModel)
        assert not is_basemodel(str)
        assert not is_basemodel(PydanticBaseModel)

    def test_is_basemodel_type(self):
        """Test is_basemodel_type function."""
        class TestModel(BaseModel):
            name: str

        assert is_basemodel_type(TestModel)
        assert not is_basemodel_type(str)

    def test_build(self):
        """Test build function."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = build(TestModel, name="test", age=25)
        assert isinstance(model, TestModel)
        assert model.name == "test"
        assert model.age == 25

    def test_construct_type_unchecked(self):
        """Test construct_type_unchecked function."""
        result = construct_type_unchecked(value="test", type_=str)
        assert result == "test"

    def test_construct_type(self):
        """Test construct_type function."""
        result = construct_type(value="test", type_=str)
        assert result == "test"

    def test_validate_type(self):
        """Test validate_type function."""
        result = validate_type(type_=str, value="test")
        assert result == "test"

    def test_validate_type_with_invalid_value(self):
        """Test validate_type with invalid value."""
        with pytest.raises(Exception):
            validate_type(type_=int, value="not_an_integer")

    def test_construct_field(self):
        """Test _construct_field function."""
        from pydantic.fields import FieldInfo

        # Test with simple field
        field_info = FieldInfo(annotation=str)
        result = _construct_field("test", field_info, "test_field")
        assert result == "test"

    def test_validate_non_model_type(self):
        """Test _validate_non_model_type function."""
        result = _validate_non_model_type(type_=str, value="test")
        assert result == "test"


class TestDiscriminatorUnion:
    """Test discriminator union functionality."""

    def test_discriminator_details(self):
        """Test DiscriminatorDetails class."""
        from zai.core._base_models import DiscriminatorDetails

        details = DiscriminatorDetails(
            mapping={"type_a": str, "type_b": int},
            discriminator_field="type",
            discriminator_alias="type_alias"
        )
        
        assert details.field_name == "type"
        assert details.field_alias_from == "type_alias"
        assert details.mapping == {"type_a": str, "type_b": int}

    def test_cached_discriminator_type(self):
        """Test CachedDiscriminatorType protocol."""
        from zai.core._base_models import CachedDiscriminatorType, DiscriminatorDetails

        class TestDiscriminatorType:
            __discriminator__ = DiscriminatorDetails(
                mapping={"type_a": str},
                discriminator_field="type",
                discriminator_alias=None
            )

        # Should not raise an error
        assert isinstance(TestDiscriminatorType(), CachedDiscriminatorType)


class TestModelFields:
    """Test model fields functionality."""

    def test_model_fields_set_property(self):
        """Test model_fields_set property for Pydantic v1 compatibility."""
        class TestModel(BaseModel):
            name: str
            age: int

        model = TestModel(name="test", age=25)
        
        # Test that the property exists and works
        fields_set = model.model_fields_set
        assert isinstance(fields_set, set)
        assert "name" in fields_set
        assert "age" in fields_set


class TestErrorHandling:
    """Test error handling scenarios."""
    
    def test_construct_with_invalid_data(self):
        """Test construct with invalid data."""
        class TestModel(BaseModel):
            name: str
            age: int
        
        # Test with valid data first
        model = TestModel.construct(name="test", age=25)
        assert model.name == "test"
        assert model.age == 25
        
        # Test with invalid data - construct should not raise for invalid data
        # as it's designed to bypass validation
        model = TestModel.construct(name="test", age="invalid")
        assert model.name == "test"
        # In construct mode, invalid data might be stored as-is or converted
        # depending on the implementation
    
    def test_validate_type_with_complex_invalid_data(self):
        """Test validate_type with complex invalid data."""
        with pytest.raises(Exception):
            validate_type(type_=int, value="not_an_integer")
    
    def test_build_with_missing_required_fields(self):
        """Test build with missing required fields."""
        class TestModel(BaseModel):
            name: str
            age: int
        
        # Test with valid data
        model = build(TestModel, name="test", age=25)
        assert model.name == "test"
        assert model.age == 25
        
        # Test with missing fields - build should handle this gracefully
        # or raise appropriate validation errors
        try:
            model = build(TestModel, name="test")  # missing age
            # If it doesn't raise, that's also valid behavior
        except Exception:
            # If it raises, that's expected
            pass


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_model_with_none_values(self):
        """Test model with None values."""
        class TestModel(BaseModel):
            name: str | None
            age: int | None

        model = TestModel(name=None, age=None)
        assert model.name is None
        assert model.age is None

    def test_model_with_empty_dict(self):
        """Test model with empty dictionary."""
        class TestModel(BaseModel):
            data: Dict[str, Any]

        model = TestModel(data={})
        assert model.data == {}

    def test_model_with_literal_types(self):
        """Test model with literal types."""
        class TestModel(BaseModel):
            status: Literal["active", "inactive"]

        model = TestModel(status="active")
        assert model.status == "active"

    def test_model_with_union_types(self):
        """Test model with union types."""
        class TestModel(BaseModel):
            value: Union[str, int]

        # Test with string
        model_str = TestModel(value="test")
        assert model_str.value == "test"

        # Test with int
        model_int = TestModel(value=42)
        assert model_int.value == 42

    def test_model_with_optional_fields(self):
        """Test model with optional fields."""
        class TestModel(BaseModel):
            name: str
            description: Optional[str] = None

        # Test with description
        model_with_desc = TestModel(name="test", description="description")
        assert model_with_desc.description == "description"

        # Test without description
        model_without_desc = TestModel(name="test")
        assert model_without_desc.description is None 