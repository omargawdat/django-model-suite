from typing import Dict, Optional

from django.http import HttpRequest

from app.admin.testmodelrelated.context import TestModelRelatedContextLogic
from app.fields.test_model_related import TestModelRelatedFields
from app.models import TestModelRelated
from django_model_suite.admin import BaseTabularInline, FieldPermissions


class TestModelRelatedInline(BaseTabularInline):
    model = TestModelRelated
    fields = ['name', 'is_active']

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
                    context.is_superuser
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
                    context.is_superuser
                ),
                editable=(
                ),
            )
        }
