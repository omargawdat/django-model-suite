from app.models import TestModelRelated
from django_model_suite.admin import BaseTabularInline, BaseStackedInline


class TestModelRelatedInline(BaseTabularInline):
    """
    Inline admin for TestModelRelated.
    
    For stacked inline, use BaseStackedInline instead:
    class TestModelRelatedInline(BaseStackedInline):
    """
    model = TestModelRelated
    extra = 1
    show_change_link = True
    can_delete = False
    view_on_site = False

    # Fields configuration
    fields = ()
    readonly_fields = ()
    autocomplete_fields = ()
