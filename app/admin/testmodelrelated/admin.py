from django.contrib import admin
from .list_view import TestModelRelatedListView
from .change_view import TestModelRelatedChangeView
from .permissions import TestModelRelatedPermissions
from .display import TestModelRelatedDisplayMixin
from app.models import TestModelRelated
from django_model_suite.adminn import BaseModelAdmin

@admin.register(TestModelRelated)
class TestModelRelatedAdmin(
    TestModelRelatedDisplayMixin,
    TestModelRelatedListView,
    TestModelRelatedChangeView,
    TestModelRelatedPermissions,
    BaseModelAdmin,
):
    pass
