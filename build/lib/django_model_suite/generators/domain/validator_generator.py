# validator_generator.py
from ..base import BaseGenerator

class ValidatorGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        content = f'''from typing import Any
from django.core.exceptions import ValidationError
from {model_import_path} import {model_name}

def validate_{self.model_name_lower}_create(*, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data

def validate_{self.model_name_lower}_update(*, instance: {model_name}, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data
'''
        self.write_file(f'{self.model_name_lower}.py', content)