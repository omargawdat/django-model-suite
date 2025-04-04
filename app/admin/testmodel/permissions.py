from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.test_model import TestModelFields
from django_model_suite.admin import FieldPermissions
from app.models import TestModel
from .context import TestModelContextLogic


class TestModelPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, test_model: Optional[TestModel] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, test_model: Optional[TestModel] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, test_model: Optional[TestModel] = None) -> Dict:
        context = TestModelContextLogic(request, test_model)

        return {
            TestModelFields.NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            )
        }
