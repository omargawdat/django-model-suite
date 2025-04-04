from app.admin.testmodelrelated.permissions import TestModelRelatedPermissions
from app.models import TestModelRelated
from django_model_suite.admin import BaseTabularInline


class TestModelRelatedInline(TestModelRelatedPermissions, BaseTabularInline):
    model = TestModelRelated
    fields = ['name', 'is_active']

