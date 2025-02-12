# selector_generator.py
from ..base import BaseGenerator

class SelectorGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        content = f'''from django.db.models import QuerySet
from {model_import_path} import {model_name}

class {model_name}Selector:
    @staticmethod
    def get_queryset() -> QuerySet:
        return {model_name}.objects.all()

    @staticmethod
    def by_id(*, id: int) -> {model_name}:
        return {model_name}Selector.get_queryset().get(id=id)
'''
        self.write_file(f'{self.model_name_lower}.py', content)