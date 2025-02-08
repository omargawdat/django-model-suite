class BookListView:
    list_display = ("id", "is_borrowed")
    list_editable = ("is_borrowed",)
    list_filter = ()
    date_hierarchy = None
    list_per_page = 50
    list_filter_submit = False
    list_fullwidth = False
    list_horizontal_scrollbar_top = False
    search_fields = ()
    search_help_text = ""
    ordering = ()

    def get_ordering(self, request):
        return ()
