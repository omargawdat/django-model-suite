# service_generator.py
from ..base import BaseGenerator

class ServiceGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        content = f'''from typing import Any
from {model_import_path} import {model_name}
from ..validators.{self.model_name_lower} import validate_{self.model_name_lower}_create, validate_{self.model_name_lower}_update

class {model_name}Service:
    @staticmethod
    def create_{self.model_name_lower}(*, data: dict[str, Any]) -> {model_name}:
        validated_data = validate_{self.model_name_lower}_create(data=data)
        instance = {model_name}.objects.create(**validated_data)
        return instance

    @staticmethod
    def update_{self.model_name_lower}(*, instance: {model_name}, data: dict[str, Any]) -> {model_name}:
        validated_data = validate_{self.model_name_lower}_update(instance=instance, data=data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_{self.model_name_lower}(*, instance: {model_name}) -> None:
        instance.delete()
'''
        self.write_file(f'{self.model_name_lower}.py', content)