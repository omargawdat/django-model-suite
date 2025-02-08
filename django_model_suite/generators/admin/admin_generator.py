# admin_generator.py
from django.apps import apps

from ..base import BaseGenerator


class AdminGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f'''from django.contrib import admin
from .list_view import {self.model_name_capital}ListView
from .change_view import {self.model_name_capital}ChangeView
from .permissions import {self.model_name_capital}Permissions
from .display import {self.model_name_capital}DisplayMixin
from {model_import_path} import {self.model_name_capital}
from django_model_suite.admin import BaseModelAdmin

@admin.register({self.model_name_capital})
class {self.model_name_capital}Admin(
    {self.model_name_capital}DisplayMixin,
    {self.model_name_capital}ListView,
    {self.model_name_capital}ChangeView,
    {self.model_name_capital}Permissions,
    BaseModelAdmin,
):
    pass
'''
        self.write_file('admin.py', content)