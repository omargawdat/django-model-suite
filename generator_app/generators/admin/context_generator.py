from typing import List

from django.apps import apps

from ..base import BaseGenerator


class ContextGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: List[str] = None) -> None:  # Add fields parameter with default None
        content = f"""from typing import Optional
from django.http import HttpRequest
from {self.model.__module__} import {self.model_name_capital}


class {self.model_name_capital}ContextLogic:
    def __init__(self, request: HttpRequest, {self.model_name_lower}: Optional[{self.model_name_capital}] = None):
        self.request = request
        self.{self.model_name_lower} = {self.model_name_lower}

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.{self.model_name_lower} is None
"""
        self.write_file('context.py', content)
