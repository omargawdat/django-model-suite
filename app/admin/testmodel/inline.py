from app.models import TestModel
from django_model_suite.admin import BaseTabularInline, BaseStackedInline
from .permissions import TestModelInlinePermissions


class TestModelInline(TestModelInlinePermissions, BaseTabularInline):
    model = TestModel
    extra = 0
    show_change_link = True
    tab = True
    fields = ()
    autocomplete_fields = ()
