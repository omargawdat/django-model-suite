from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from import_export.formats.base_formats import CSV
from unfold.contrib.import_export.forms import ExportForm
from .list_view import TestModelListView
from .change_view import TestModelChangeView
from .permissions import TestModelAdminPermissions
from .display import TestModelDisplayMixin
from .resource import TestModelResource
from app.models import TestModel
from django_model_suite.admin import BaseModelAdmin

@admin.register(TestModel)
class TestModelAdmin(
    TestModelDisplayMixin,
    TestModelListView,
    TestModelChangeView,
    TestModelAdminPermissions,
    BaseModelAdmin,
):
    resource_class = TestModelResource
    export_form_class = ExportForm
    formats = [CSV]
