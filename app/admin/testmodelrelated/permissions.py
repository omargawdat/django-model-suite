from typing import Optional, Dict

from django.http import HttpRequest

from app.models import TestModelRelated
from django_model_suite.admin import FieldPermissions
from .context import TestModelRelatedContextLogic
from ...fields.test_model_related import TestModelRelatedFields


class TestModelRelatedPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return True

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
                    context.is_superuser

                ),
            ),
            TestModelRelatedFields.NAME: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                    context.is_superuser

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
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.CREATED_AT: FieldPermissions(
                visible=(
                ),
                editable=(
                ),
            ),
            TestModelRelatedFields.NEW_FILED: FieldPermissions(
                visible=(
                ),
                editable=(
                ),
            )
        }
