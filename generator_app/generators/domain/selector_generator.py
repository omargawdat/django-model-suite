from django.apps import apps

from ..base import BaseGenerator


class SelectorGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.output_path = "domain/selectors"
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f'''from django.db.models import QuerySet
from {model_import_path} import {self.model_name_capital}

class {self.model_name_capital}Selector:
    @staticmethod
    def get_queryset() -> QuerySet:
        return {self.model_name_capital}.objects.all()

    @staticmethod
    def by_id(*, id: int) -> {self.model_name_capital}:
        return {self.model_name_capital}Selector.get_queryset().get(id=id)
'''
        self.write_file(f'{self.model_name_lower}.py', content)