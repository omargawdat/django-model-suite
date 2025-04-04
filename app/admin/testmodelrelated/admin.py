from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .list_view import TestModelRelatedListView
from .change_view import TestModelRelatedChangeView
from .permissions import TestModelRelatedPermissions
from .display import TestModelRelatedDisplayMixin
from .resource import TestModelRelatedResource
from app.models import TestModelRelated
from django_model_suite.admin import BaseModelAdmin

@admin.register(TestModelRelated)
class TestModelRelatedAdmin(
    TestModelRelatedDisplayMixin,
    TestModelRelatedListView,
    TestModelRelatedChangeView,
    TestModelRelatedPermissions,
    ImportExportModelAdmin,
    BaseModelAdmin,
):
    resource_class = TestModelRelatedResource
