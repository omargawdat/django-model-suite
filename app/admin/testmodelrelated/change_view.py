class TestModelRelatedChangeView:
    filter_horizontal = ()
    compressed_fields = True
    autocomplete_fields = ()
    fieldsets = (
        ("Information", {"fields": ("name", "test_model")}),
    )
