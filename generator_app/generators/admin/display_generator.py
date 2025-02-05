from ..base import BaseGenerator


class DisplayGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''from unfold.decorators import display
from apps.{self.app_name}.models import {self.model_name_capital}

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
