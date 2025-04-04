from typing import Any
from django.core.exceptions import ValidationError
from app.models import TestModel

def validate_test_model_create(*, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data

def validate_test_model_update(*, instance: TestModel, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data
