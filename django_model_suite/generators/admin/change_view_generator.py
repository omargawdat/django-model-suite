from ..base import BaseGenerator


class ChangeViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''class {self.model_name_capital}ChangeView:
    filter_horizontal = ()
    compressed_fields = True
    autocomplete_fields = ()
    fieldsets = (
        ("Information", {{"fields": ()}}),
    )
'''
        self.write_file('change_view.py', content)