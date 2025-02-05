import os
from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        self.app_name = app_name
        self.model_name = model_name
        self.base_path = base_path
        self.model_name_capital = model_name.capitalize()
        self.model_name_lower = model_name.lower()
        self.is_domain = any(x in base_path for x in ['selectors', 'services', 'validators'])
        self.output_path = "" if self.is_domain else self.model_name_lower

    def _ensure_directory_exists(self, directory_path: str) -> None:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    def _create_init_file(self, directory_path: str) -> None:
        init_file = os.path.join(directory_path, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write("")

    def write_file(self, filename: str, content: str) -> None:
        """Write content to a file with proper directory structure."""
        if self.is_domain:
            # For domain components, write directly to base_path
            target_dir = self.base_path
            full_path = os.path.join(target_dir, f"{self.model_name_lower}.py")
        else:
            # For admin and api, use model-specific subdirectories
            target_dir = os.path.join(self.base_path, self.model_name_lower)
            full_path = os.path.join(target_dir, filename)

        self._ensure_directory_exists(target_dir)
        self._create_init_file(target_dir)

        with open(full_path, 'w') as f:
            f.write(content)

    @abstractmethod
    def generate(self, fields: list) -> None:
        pass
