import os

from django.apps import apps


def get_model_fields(app_name: str, model_name: str) -> list:
    """Get all fields from a model, including relations."""
    model = apps.get_model(app_name, model_name)
    return [field.name for field in model._meta.get_fields()]

def ensure_package(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    init_file = os.path.join(path, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w"):
            pass
