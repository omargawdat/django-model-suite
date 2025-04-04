from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.test_model_related import TestModelRelatedFields
from django_model_suite.admin import FieldPermissions
from app.models import TestModelRelated
from .context import TestModelRelatedContextLogic


class TestModelRelatedPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, test_model_related: Optional[TestModelRelated] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, test_model_related: Optional[TestModelRelated] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, test_model_related: Optional[TestModelRelated] = None) -> Dict:
        context = TestModelRelatedContextLogic(request, test_model_related)

        return {
            TestModelRelatedFields.TEST_MODEL: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.DESCRIPTION: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.IS_ACTIVE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.CREATED_AT: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.NEW_FILED: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            )
        }
