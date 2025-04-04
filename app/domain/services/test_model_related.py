from typing import Any
from app.models import TestModelRelated
from ..validators.test_model_related import validate_test_model_related_create, validate_test_model_related_update

class TestModelRelatedService:
    @staticmethod
    def create_test_model_related(*, data: dict[str, Any]) -> TestModelRelated:
        validated_data = validate_test_model_related_create(data=data)
        instance = TestModelRelated.objects.create(**validated_data)
        return instance

    @staticmethod
    def update_test_model_related(*, instance: TestModelRelated, data: dict[str, Any]) -> TestModelRelated:
        validated_data = validate_test_model_related_update(instance=instance, data=data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_test_model_related(*, instance: TestModelRelated) -> None:
        instance.delete()
