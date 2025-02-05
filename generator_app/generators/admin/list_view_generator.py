from ..base import BaseGenerator


class ListViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''class {self.model_name_capital}ListView:
    LIST_DISPLAY = ()
    LIST_FILTER = ()
    DATE_HIERARCHY = None
    LIST_PER_PAGE = 50
    LIST_FILTER_SUBMIT = False
    LIST_FULLWIDTH = False
    LIST_HORIZONTAL_SCROLLBAR_TOP = False
    SEARCH_FIELDS = ()
    SEARCH_HELP_TEXT = ""
    ORDERING = ()

    def get_ordering(self, request):
        return ()
'''
        self.write_file('list_view.py', content)
