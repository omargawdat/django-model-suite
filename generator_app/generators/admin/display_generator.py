from django.apps import apps

from ..base import BaseGenerator


class DisplayGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f'''from unfold.decorators import display
from {model_import_path} import {self.model_name_capital}

class {self.model_name_capital}DisplayMixin:
    @display(description="{self.model_name_lower}", header=True)
    def display_header(self, {self.model_name_lower}: {self.model_name_capital}):
        """Display header with image if available."""
        return [
            {self.model_name_lower}.pk,
            "",
            "O",
            {{"path": {self.model_name_lower}.image.url if hasattr({self.model_name_lower}, 'image') and {self.model_name_lower}.image else None}},
        ]
'''
        self.write_file('display.py', content)