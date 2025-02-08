from typing import List
from django.apps import apps
from ..base import BaseGenerator


class PermissionsGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: List[str]) -> None:
        field_rules = [
            f"            {self.model_name_capital}Fields.{field.upper()}: FieldPermissions(\n"
            "                visible=(\n"
            "                    context.is_superuser\n"
            "                ),\n"
            "                editable=(\n"
            "                ),\n"
            "            )" for field in fields
        ]

        content = f"""from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.{self.model_name_lower} import {self.model_name_capital}Fields
from ....core.admin import FieldPermissions
from {self.model.__module__} import {self.model_name_capital}
from .context import {self.model_name_capital}ContextLogic


class {self.model_name_capital}Permissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{self.model_name_capital}] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{self.model_name_capital}] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, {self.model_name_lower}: Optional[{self.model_name_capital}] = None) -> Dict:
        context = {self.model_name_capital}ContextLogic(request, {self.model_name_lower})

        return {{
""" + ',\n'.join(field_rules) + """
        }
"""
        self.write_file('permissions.py', content)