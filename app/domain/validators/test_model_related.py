from typing import Any
from django.core.exceptions import ValidationError
from app.models import TestModelRelated

def validate_test_model_related_create(*, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data

def validate_test_model_related_update(*, instance: TestModelRelated, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data
