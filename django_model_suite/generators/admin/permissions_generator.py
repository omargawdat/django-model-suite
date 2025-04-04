# permissions_generator.py
import re
from typing import List

from ..base import BaseGenerator


class PermissionsGenerator(BaseGenerator):
    def generate(self, fields: List[str]) -> None:
        model_name = self.model.__name__
        field_rules = [
            f"            {model_name}Fields.{field.upper()}: FieldPermissions(\n"
            "                visible=(\n"
            "                    context.is_superuser\n"
            "                ),\n"
            "                editable=(\n"
            "                ),\n"
            "            )" for field in fields
        ]

        content = f"""from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.{self.model_name_lower} import {model_name}Fields
from django_model_suite.admin import FieldPermissions
from {self.model.__module__} import {model_name}
from .context import {model_name}ContextLogic


class {model_name}Permissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, {self.model_name_lower}: Optional[{model_name}] = None) -> Dict:
        context = {model_name}ContextLogic(request, {self.model_name_lower})

        return {{
""" + ',\n'.join(field_rules) + """
        }
"""
        def update_permissions(existing_content):
            """Update existing permissions file with any new fields."""
            # Skip if no existing content
            if not existing_content.strip():
                return content
                
            # Extract existing fields from the file
            existing_fields = []
            field_pattern = rf"{model_name}Fields\.([A-Z_]+)"
            for line in existing_content.split('\n'):
                match = re.search(field_pattern, line)
                if match:
                    existing_fields.append(match.group(1))
            
            # Find fields that need to be added (convert to uppercase for comparison)
            new_fields = [field for field in fields if field.upper() not in existing_fields]
            
            # If no new fields, return the existing content
            if not new_fields:
                return existing_content
                
            # Generate rules for new fields
            new_field_rules = []
            for i, field in enumerate(new_fields):
                rule = f"            {model_name}Fields.{field.upper()}: FieldPermissions(\n"
                rule += "                visible=(\n"
                rule += "                    context.is_superuser\n"
                rule += "                ),\n"
                rule += "                editable=(\n"
                rule += "                ),\n"
                rule += "            )"
                
                # Add a comma if this isn't the last field
                if i < len(new_fields) - 1:
                    rule += ","
                    
                new_field_rules.append(rule)
            
            # Find where to insert the new fields
            lines = existing_content.split('\n')
            
            # Look for the return statement and the closing brace
            return_idx = -1
            closing_brace_idx = -1
            
            for i, line in enumerate(lines):
                if "return {" in line:
                    return_idx = i
                    break
            
            if return_idx == -1:
                # Can't find where to insert, return new content
                return content
                
            # Find closing brace after return
            for i, line in enumerate(lines[return_idx:], return_idx):
                if '}' in line and not '"' in line and not "'" in line:  # Avoid matching braces in strings
                    closing_brace_idx = i
                    break
            
            if closing_brace_idx == -1:
                # Can't find closing brace, return new content
                return content
                
            # Determine if we need to add a comma to the last existing field
            needs_comma = False
            for i in range(closing_brace_idx - 1, return_idx, -1):
                line = lines[i].strip()
                if line and not line.endswith(',') and not line.startswith('#'):
                    lines[i] = lines[i] + ','
                    break
                elif line and (line.endswith(',') or line.endswith('{')):
                    # Already has a comma or is the opening brace
                    break
                
            # Insert new fields before the closing brace
            new_content = (
                lines[:closing_brace_idx] + 
                new_field_rules + 
                lines[closing_brace_idx:]
            )
            
            return '\n'.join(new_content)
            
        # Use update_file instead of write_file to handle existing files
        self.update_file('permissions.py', content, update_permissions)