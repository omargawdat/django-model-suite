from app.admin.testmodelrelated.permissions import TestModelRelatedInlinePermissions
from app.models import TestModelRelated
from django_model_suite.admin import BaseTabularInline


class TestModelRelatedInline(TestModelRelatedInlinePermissions, BaseTabularInline):
    model = TestModelRelated
    fields = ['name', 'is_active']

