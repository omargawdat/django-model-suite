from ..base import BaseGenerator


class PermissionsGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        field_rules = [
            f'''            {self.model_name_capital}Fields.{field.upper()}: FieldPermissions(
                visible=False,
                editable=False,
            )''' for field in fields
        ]

        content = f'''from dataclasses import dataclass
from .fields import {self.model_name_capital}Fields


@dataclass
class FieldPermissions:
    visible: bool = False
    editable: bool = False


class {self.model_name_capital}Permissions:
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_field_rules(self, request, obj=None):
        is_superuser = request.user.is_superuser
        return {{
{",".join(field_rules)}
        }}
'''
        self.write_file('permissions.py', content)
