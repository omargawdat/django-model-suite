from django.contrib import admin

from app.models import TestModelRelated
from django_model_suite.admin import BaseModelAdmin
from .change_view import TestModelRelatedChangeView
from .display import TestModelRelatedDisplayMixin
from .list_view import TestModelRelatedListView
from .permissions import TestModelRelatedPermissions


@admin.register(TestModelRelated)
class TestModelRelatedAdmin(
    TestModelRelatedDisplayMixin,
    TestModelRelatedListView,
    TestModelRelatedChangeView,
    TestModelRelatedPermissions,
    # ImportExportModelAdmin,
    BaseModelAdmin,
):
    inlines = []
