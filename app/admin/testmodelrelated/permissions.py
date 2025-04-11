from typing import Optional, Dict

from django.http import HttpRequest

from app.models import TestModelRelated
from django_model_suite.admin import FieldPermissions, AdminContextLogic
from ...fields.test_model_related import TestModelRelatedFields


class BaseTestModelRelatedPermissions:
    def get_field_rules(self, request: HttpRequest, test_model_related: Optional[TestModelRelated] = None) -> Dict:
        # Define context variables
        super_admin = AdminContextLogic.is_super_admin(request)
        normal_admin = AdminContextLogic.is_normal_admin(request)
        created = AdminContextLogic.is_object_created(test_model_related)

        return {
            TestModelRelatedFields.TEST_MODEL: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.NAME: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.DESCRIPTION: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.IS_ACTIVE: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.CREATED_AT: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.NEW_FILED: FieldPermissions(
                visible=(
                    normal_admin
                ),
                editable=(
                ),
            )
        }


class TestModelRelatedAdminPermissions(BaseTestModelRelatedPermissions):
    def can_add(self, request, obj=None):
        return True

    def can_change(self, request, obj=None):
        return True

    def can_delete(self, request, obj=None):
        return False


class TestModelRelatedInlinePermissions(BaseTestModelRelatedPermissions):
    def can_add(self, request, obj=None):
        return True

    def can_change(self, request, obj=None):
        return True

    def can_delete(self, request, obj=None):
        return False
