from django.conf import settings

from ..base import BaseGenerator


class AdminGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"

        # Get BaseModelAdmin import path from settings or use default
        base_model_admin_path = getattr(settings, 'BASE_MODEL_ADMIN_PATH')
        
        content = f'''from django.contrib import admin
from .list_view import {model_name}ListView
from .change_view import {model_name}ChangeView
from .permissions import {model_name}Permissions
from .display import {model_name}DisplayMixin
from {model_import_path} import {model_name}
from {base_model_admin_path} import BaseModelAdmin

@admin.register({model_name})
class {model_name}Admin(
    {model_name}DisplayMixin,
    {model_name}ListView,
    {model_name}ChangeView,
    {model_name}Permissions,
    BaseModelAdmin,
):
    pass
'''
        self.write_file('admin.py', content)