from ..base import BaseGenerator


class AdminGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''from django.contrib import admin
from common.base.basemodeladmin import BaseModelAdmin
from .list_view import {self.model_name_capital}ListView
from .change_view import {self.model_name_capital}ChangeView
from .permissions import {self.model_name_capital}Permissions
from .display import {self.model_name_capital}DisplayMixin
from .fields import {self.model_name_capital}Fields
from apps.{self.app_name}.models import {self.model_name_capital}


@admin.register({self.model_name_capital})
class {self.model_name_capital}Admin(
    BaseModelAdmin,
    {self.model_name_capital}DisplayMixin,
    {self.model_name_capital}ListView,
    {self.model_name_capital}ChangeView,
    {self.model_name_capital}Permissions
):
    pass
'''
        self.write_file('admin.py', content)
