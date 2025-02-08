from ..base import BaseGenerator


class ListViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''class {self.model_name_capital}ListView:
    list_display = ()
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
'''
        self.write_file('list_view.py', content)