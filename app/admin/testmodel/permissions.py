from typing import Optional, Dict

from django.http import HttpRequest

from app.models import TestModel
from django_model_suite.admin import FieldPermissions
from .context import TestModelContextLogic
from ...fields.test_model import TestModelFields


class TestModelPermissions:
    def _has_custom_add_permission(self, request, obj=None):
        return True

    def _has_custom_change_permission(self, request, obj=None):
        return True

    def _has_custom_delete_permission(self, request, obj=None):
        return True

    def get_field_rules(self, request: HttpRequest, test_model: Optional[TestModel] = None) -> Dict:
        context = TestModelContextLogic(request, test_model)

        return {
            TestModelFields.NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser

                ),
            )
        }
