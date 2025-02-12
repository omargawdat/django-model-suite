# context_generator.py
from typing import List
from ..base import BaseGenerator

class ContextGenerator(BaseGenerator):
    def generate(self, fields: List[str] = None) -> None:
        model_name = self.model.__name__
        content = f"""from typing import Optional
from django.http import HttpRequest
from {self.model.__module__} import {model_name}


class {model_name}ContextLogic:
    def __init__(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None):
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