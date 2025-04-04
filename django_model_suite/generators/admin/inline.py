from ..base import BaseGenerator


class InlineAdminGenerator(BaseGenerator):
    def generate(self, fields: list = None) -> None:
        """
        Generate inline admin class for a model.
        
        Args:
            fields: List of fields to include in the inline (defaults to empty)
        """
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        
        # Import both base classes but use BaseTabularInline by default
        base_imports = "from django_model_suite.admin import BaseTabularInline, BaseStackedInline"
            
        content = f'''from {model_import_path} import {model_name}
{base_imports}


class {model_name}Inline(BaseTabularInline):
    """
    Inline admin for {model_name}.
    
    For stacked inline, use BaseStackedInline instead:
    class {model_name}Inline(BaseStackedInline):
    """
    model = {model_name}
    extra = 1
    show_change_link = True
    can_delete = False
    view_on_site = False

    # Fields configuration
    fields = ()
    readonly_fields = ()
    autocomplete_fields = ()
'''
        self.write_file('inline.py', content)
