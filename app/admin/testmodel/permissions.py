from typing import Optional, Dict

from django.http import HttpRequest

from app.models import TestModel
from django_model_suite.admin import FieldPermissions
from .context import TestModelContextLogic
from ...fields.test_model import TestModelFields


class BaseTestModelPermissions:
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


class TestModelAdminPermissions(BaseTestModelPermissions):
    def can_add(self, request, obj=None):
        return True

    def can_change(self, request, obj=None):
        return False

    def can_delete(self, request, obj=None):
        return False


class TestModelInlinePermissions(BaseTestModelPermissions):
    def can_add(self, request, obj=None):
        return False

    def can_change(self, request, obj=None):
        return False

    def can_delete(self, request, obj=None):
        return False
