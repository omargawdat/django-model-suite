from typing import Any
from app.models import TestModel
from ..validators.test_model import validate_test_model_create, validate_test_model_update

class TestModelService:
    @staticmethod
    def create_test_model(*, data: dict[str, Any]) -> TestModel:
        validated_data = validate_test_model_create(data=data)
        instance = TestModel.objects.create(**validated_data)
        return instance

    @staticmethod
    def update_test_model(*, instance: TestModel, data: dict[str, Any]) -> TestModel:
        validated_data = validate_test_model_update(instance=instance, data=data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_test_model(*, instance: TestModel) -> None:
        instance.delete()
