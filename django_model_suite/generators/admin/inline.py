from ..base import BaseGenerator


class InlineAdminGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"

        content = f'''from django.contrib import admin
from {model_import_path} import {model_name}

class {model_name}Inline(admin.TabularInline):
    model = {model_name}
    extra = 1
    show_change_link = True
    can_delete = False
    view_on_site = False

    # Fields configuration
    fields = ()
    readonly_fields = ()
    autocomplete_fields = ()

    # Display settings
    max_num = None
    min_num = None

    # Permissions
    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
'''
        self.write_file('inline_admin.py', content)
