from ..base import BaseGenerator


class InlineAdminGenerator(BaseGenerator):
    def generate(self, fields: list = None) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        
        # Import both base classes but use BaseTabularInline by default
        base_imports = "from django_model_suite.admin import BaseTabularInline, BaseStackedInline"
            
        content = f'''from {model_import_path} import {model_name}
{base_imports}


class {model_name}Inline(BaseTabularInline):
    model = {model_name}
    extra = 0
    show_change_link = True
    fields = ()
    autocomplete_fields = ()
'''
        self.write_file('inline.py', content)
