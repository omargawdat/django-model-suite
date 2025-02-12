# permissions_generator.py
from typing import List

from ..base import BaseGenerator


class PermissionsGenerator(BaseGenerator):
    def generate(self, fields: List[str]) -> None:
        model_name = self.model.__name__
        field_rules = [
            f"            {model_name}Fields.{field.upper()}: FieldPermissions(\n"
            "                visible=(\n"
            "                    context.is_superuser\n"
            "                ),\n"
            "                editable=(\n"
            "                ),\n"
            "            )" for field in fields
        ]

        content = f"""from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.{self.model_name_lower} import {model_name}Fields
from django_model_suite.admin import FieldPermissions
from {self.model.__module__} import {model_name}
from .context import {model_name}ContextLogic


class {model_name}Permissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> Dict:
        context = {model_name}ContextLogic(request, {self.model_name_lower})

        return {{
""" + ',\n'.join(field_rules) + """
        }
"""
        self.write_file('permissions.py', content)