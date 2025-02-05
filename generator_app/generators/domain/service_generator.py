# service_generator.py
from ..base import BaseGenerator


class ServiceGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.output_path = "domain/services"

    def generate(self, fields: list) -> None:
        content = f'''from typing import Any
from {self.model_name_capital} import {self.model_name_capital}

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
