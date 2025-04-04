from django.conf import settings
import os.path

from ..base import BaseGenerator


class AdminGenerator(BaseGenerator):
    def generate(self, fields: list, has_inline: bool = False) -> None:
        """
        Generate admin class for a model.
        
        Args:
            fields: List of fields to include in the admin
            has_inline: Whether to include inline import
        """
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"

        # Get BaseModelAdmin import path from settings or use default
        base_model_admin_path = getattr(settings, 'BASE_MODEL_ADMIN_PATH')
        
        # Check if inline file exists to potentially import it
        inline_import = ""
        if has_inline or os.path.exists(os.path.join(self.base_path, 'inline.py')):
            inline_import = f"from .inline import {model_name}Inline"
        
        content = f'''from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .list_view import {model_name}ListView
from .change_view import {model_name}ChangeView
from .permissions import {model_name}Permissions
from .display import {model_name}DisplayMixin
from .resource import {model_name}Resource
from {model_import_path} import {model_name}
from {base_model_admin_path} import BaseModelAdmin
{inline_import}

@admin.register({model_name})
class {model_name}Admin(
    {model_name}DisplayMixin,
    {model_name}ListView,
    {model_name}ChangeView,
    {model_name}Permissions,
    ImportExportModelAdmin,
    BaseModelAdmin,
):
    resource_class = {model_name}Resource
    
    {f"inlines = [{model_name}Inline]" if has_inline or inline_import else ""}
'''
        self.write_file('admin.py', content)