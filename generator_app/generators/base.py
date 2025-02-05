import os
from abc import ABC, abstractmethod

from generator_app.generators.model_utils import ensure_package


class BaseGenerator(ABC):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        self.app_name = app_name
        self.model_name = model_name
        self.base_path = base_path
        self.model_name_capital = model_name.capitalize()
        self.model_name_lower = model_name.lower()

    def write_file(self, filename: str, content: str) -> None:
        target_dir = self.base_path
        full_path = os.path.join(target_dir, filename)

        ensure_package(target_dir)
        if os.path.exists(full_path):
            return

        with open(full_path, "w") as f:
            f.write(content)

    @abstractmethod
    def generate(self, fields: list) -> None:
        pass