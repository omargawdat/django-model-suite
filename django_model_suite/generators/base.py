import os
import re
from abc import ABC, abstractmethod

from django_model_suite.generators.model_utils import ensure_package


class BaseGenerator(ABC):
    def __init__(self, app_name: str, model_name: str, base_path: str, model_class):
        self.base_path = base_path
        self.model = model_class
        self.model_name_lower = self._to_snake_case(self.model.__name__)

    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case (e.g., TestModelRelated -> test_model_related)"""
        pattern = re.compile(r'(?<!^)(?=[A-Z])')

        return pattern.sub('_', name).lower()

    def write_file(self, filename: str, content: str) -> None:
        """
        Write content to a file only if the file doesn't already exist.
        """
        target_dir = self.base_path
        full_path = os.path.join(target_dir, filename)

        ensure_package(target_dir)
        if os.path.exists(full_path):
            return

        with open(full_path, "w") as f:
            f.write(content)
            
    def update_file(self, filename: str, content: str, update_func=None) -> None:
        """
        Write content to a file, or update it if it already exists using update_func.
        
        Args:
            filename: The name of the file to write/update
            content: The content to write if the file doesn't exist
            update_func: A function that takes the existing content and returns updated content
                        If None, will overwrite the file
        """
        target_dir = self.base_path
        full_path = os.path.join(target_dir, filename)

        ensure_package(target_dir)
        
        if os.path.exists(full_path):
            if update_func:
                with open(full_path, "r") as f:
                    existing_content = f.read()
                
                updated_content = update_func(existing_content)
                
                with open(full_path, "w") as f:
                    f.write(updated_content)
        else:
            # File doesn't exist, create it
            with open(full_path, "w") as f:
                f.write(content)

    @abstractmethod
    def generate(self, fields: list) -> None:
        pass