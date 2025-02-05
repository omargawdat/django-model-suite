from django.apps import apps

from ..base import BaseGenerator


class ValidatorGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.output_path = "domain/validators"
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f'''from typing import Any
from django.core.exceptions import ValidationError
from {model_import_path} import {self.model_name_capital}

def validate_{self.model_name_lower}_create(*, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data

def validate_{self.model_name_lower}_update(*, instance: {self.model_name_capital}, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data
'''
        self.write_file(f'{self.model_name_lower}.py', content)