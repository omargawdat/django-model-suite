from django_model_suite.generators.base import BaseGenerator

class FilterGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        content = f"""from django_filters import rest_framework as filters

class {model_name}Filter(filters.FilterSet):
    pass
"""
        file_name = "filters.py"
        self.write_file(file_name, content)