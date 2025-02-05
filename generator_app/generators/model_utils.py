from django.apps import apps


def get_model_fields(app_name: str, model_name: str) -> list:
    """Get non-relational fields from a model."""
    model = apps.get_model(app_name, model_name)
    return [field.name for field in model._meta.get_fields() if not field.is_relation]


def get_model(app_name: str, model_name: str):
    """Get model class."""
    return apps.get_model(app_name, model_name)
