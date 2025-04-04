from app.models import TestModel
from django_model_suite.admin import BaseTabularInline


class TestModelInline(BaseTabularInline):
    """
    Inline admin for TestModel.
    
    For stacked inline, use BaseStackedInline instead:
    class TestModelInline(BaseStackedInline):
    """
    model = TestModel
    extra = 1
    show_change_link = True
    can_delete = False
    view_on_site = False

    # Fields configuration
    fields = ()
    readonly_fields = ()
    autocomplete_fields = ()
