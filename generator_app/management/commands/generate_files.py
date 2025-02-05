import os

from django.apps import apps
from django.core.management import BaseCommand

from generator_app.generators.factory import GeneratorFactory
from generator_app.generators.model_utils import get_model_fields


class Command(BaseCommand):
    help = "Generates admin, API, and domain files for Django apps"

    COMPONENT_CONFIGS = {
        "admin": {"path": "admin"},
        "api": {"path": "api"},
        "selectors": {"path": "domain/selectors"},
        "services": {"path": "domain/services"},
        "validators": {"path": "domain/validators"},
    }

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="Name of the app (e.g., user)")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def get_app_path(self, app_name: str) -> str:
        """Retrieve the full file-system path for the given app."""
        try:
            app_config = apps.get_app_config(app_name)
            app_path = os.path.dirname(app_config.module.__file__)
            self.stdout.write(f"Found app path: {app_path}")
            return app_path
        except LookupError:
            raise ValueError(f"App '{app_name}' not found in INSTALLED_APPS")

    @staticmethod
    def ensure_package_path(path: str) -> None:
        """
        Ensure that the directory exists and contains an __init__.py file.
        (This makes the directory a valid Python package.)
        """
        os.makedirs(path, exist_ok=True)
        init_file = os.path.join(path, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write("")

    def handle(self, *args, **options):
        app_name = options["app_name"]
        model_name = options["model_name"]

        try:
            app_path = self.get_app_path(app_name)
            if not app_path:
                raise ValueError("App path cannot be empty")

            fields = get_model_fields(app_name, model_name)

            for component, config in self.COMPONENT_CONFIGS.items():
                self._generate_component(
                    app_path, app_name, model_name, component, config["path"], fields
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully generated files for model '{model_name}'"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

    def _generate_component(
            self,
            app_path: str,
            app_name: str,
            model_name: str,
            component: str,
            component_path: str,
            fields: list,
    ) -> None:
        base_path = os.path.join(app_path, component_path)
        self.stdout.write(f"Generating {component} in {base_path}")

        # Ensure the target directories are valid Python packages.
        self.ensure_package_path(app_path)
        self.ensure_package_path(base_path)

        generators = GeneratorFactory.create_generators(
            app_name, model_name, base_path, component
        )
        for generator in generators:
            generator.generate(fields)