from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from import_export.formats.base_formats import CSV
from unfold.contrib.import_export.forms import ExportForm

from app.models import TestModel
from django_model_suite.admin import BaseModelAdmin
from .change_view import TestModelChangeView
from .display import TestModelDisplayMixin
from .list_view import TestModelListView
from .permissions import TestModelPermissions
from .resource import TestModelResource
from ..testmodelrelated.inline import TestModelRelatedInline


@admin.register(TestModel)
class TestModelAdmin(
    TestModelDisplayMixin,
    TestModelListView,
    TestModelChangeView,
    TestModelPermissions,
    ExportActionModelAdmin,
    BaseModelAdmin,
):
    resource_class = TestModelResource
    export_form_class = ExportForm
    formats = [CSV]
    inlines = [TestModelRelatedInline]
