from ..base import BaseGenerator


class ChangeViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''class {self.model_name_capital}ChangeView:
    FILTER_HORIZONTAL = ()
    COMPRESSED_FIELDS = False
    AUTOCOMPLETE_FIELDS = ()
    FIELDSETS = (
        ("Information", {{"fields": ()}}),
    )
'''
        self.write_file('change_view.py', content)
