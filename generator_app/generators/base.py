import os
from abc import ABC, abstractmethod

import os
from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        self.app_name = app_name
        self.model_name = model_name
        self.base_path = base_path
        self.model_name_capital = model_name.capitalize()
        self.model_name_lower = model_name.lower()
        # Domain generators write directly to the provided base_path.
        self.is_domain = any(x in base_path for x in ['selectors', 'services', 'validators'])
        # For non-domain generators, we use a subdirectory named after the model.
        self.output_path = "" if self.is_domain else self.model_name_lower

    def ensure_package_dir(self, directory_path: str) -> None:
        """
        Ensure that a directory exists and that an __init__.py file is present,
        making it a Python package.
        """
        os.makedirs(directory_path, exist_ok=True)
        init_file = os.path.join(directory_path, "__init__.py")
        # Only create __init__.py if it does not exist.
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write("")

    def write_file(self, filename: str, content: str) -> None:
        """
        Write the given content to a file with proper directory structure.
        - For domain generators: writes directly to base_path with a fixed filename.
        - For admin/API generators: writes to a subdirectory named after the model.

        If the target file already exists, it will not be overwritten.
        """
        if self.is_domain:
            target_dir = self.base_path
            full_path = os.path.join(target_dir, f"{self.model_name_lower}.py")
        else:
            target_dir = os.path.join(self.base_path, self.model_name_lower)
            full_path = os.path.join(target_dir, filename)

        self.ensure_package_dir(target_dir)
        if os.path.exists(full_path):
            # File exists; skip writing.
            return

        with open(full_path, "w") as f:
            f.write(content)

    @abstractmethod
    def generate(self, fields: list) -> None:
        """Generate file(s) using the provided model fields."""
        pass