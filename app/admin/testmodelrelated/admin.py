from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.models import TestModelRelated
from django_model_suite.admin import BaseModelAdmin
from .change_view import TestModelRelatedChangeView
from .display import TestModelRelatedDisplayMixin
from .inline import TestModelRelatedInline
from .list_view import TestModelRelatedListView
from .permissions import TestModelRelatedPermissions
from .resource import TestModelRelatedResource


@admin.register(TestModelRelated)
class TestModelRelatedAdmin(
    TestModelRelatedDisplayMixin,
    TestModelRelatedListView,
    TestModelRelatedChangeView,
    TestModelRelatedPermissions,
    # ImportExportModelAdmin,
    BaseModelAdmin,
):
    # resource_class = TestModelRelatedResource

    inlines = []
