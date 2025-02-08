# service_generator.py
from django.apps import apps

from ..base import BaseGenerator


class ServiceGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.output_path = "domain/services"
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f'''from typing import Any
from {model_import_path} import {self.model_name_capital}
from ..validators.book import validate_book_create, validate_book_update

class {self.model_name_capital}Service:
    @staticmethod
    def create_{self.model_name_lower}(*, data: dict[str, Any]) -> {self.model_name_capital}:
        validated_data = validate_{self.model_name_lower}_create(data=data)
        instance = {self.model_name_capital}.objects.create(**validated_data)
        return instance

    @staticmethod
    def update_{self.model_name_lower}(*, instance: {self.model_name_capital}, data: dict[str, Any]) -> {self.model_name_capital}:
        validated_data = validate_{self.model_name_lower}_update(instance=instance, data=data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_{self.model_name_lower}(*, instance: {self.model_name_capital}) -> None:
        instance.delete()
'''
        self.write_file(f'{self.model_name_lower}.py', content)