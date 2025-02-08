from generator_app.generators.base import BaseGenerator


class FilterGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f"""from django_filters import rest_framework as filters

class {self.model_name_capital}Filter(filters.FilterSet):
    pass
"""
        file_name = "filters.py"
        self.write_file(file_name, content)
