from app.models import TestModel
from django_model_suite.admin import BaseTabularInline, BaseStackedInline


class TestModelInline(BaseTabularInline):
    model = TestModel
    extra = 1
    show_change_link = True
    can_delete = False
    view_on_site = False

    # Fields configuration
    fields = ()
    readonly_fields = ()
    autocomplete_fields = ()
