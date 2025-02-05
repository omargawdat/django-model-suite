import os
from django.core.management import BaseCommand
from django.apps import apps

from generator_app.generators.factory import GeneratorFactory
from generator_app.generators.model_utils import get_model_fields


class Command(BaseCommand):
    help = "Generates admin, API, and domain files for Django apps"

    COMPONENT_CONFIGS = {
        "admin": {"path": "admin"},
        "api": {"path": "api"},
        "selectors": {"path": "domain/selectors"},
        "services": {"path": "domain/services"},
        "validators": {"path": "domain/validators"}
    }

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="Name of the app (e.g., user)")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def get_app_path(self, app_name: str) -> str:
        """Get the full path of the app using Django's app registry."""
        try:
            app_config = apps.get_app_config(app_name)
            app_path = os.path.dirname(app_config.module.__file__)
            self.stdout.write(f"Found app path: {app_path}")
            return app_path
        except LookupError:
            raise ValueError(f"App '{app_name}' not found in INSTALLED_APPS")

    def handle(self, *args, **options):
        app_name = options["app_name"]
        model_name = options["model_name"]

        try:
            app_path = self.get_app_path(app_name)
            if not app_path:
                raise ValueError("App path cannot be empty")

            fields = get_model_fields(app_name, model_name)

            for component in self.COMPONENT_CONFIGS.keys():
                self._generate_component(app_path, app_name, model_name, component, fields)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully generated files for {model_name}"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e!s}"))

    def _ensure_directory_exists(self, directory_path: str) -> None:
        """Create directory if it doesn't exist."""
        if not directory_path:
            raise ValueError("Directory path cannot be empty")

        if not os.path.exists(directory_path):
            self.stdout.write(f"Creating directory: {directory_path}")
            os.makedirs(directory_path)

    def _create_init_file(self, directory_path: str) -> None:
        """Create __init__.py file if it doesn't exist."""
        if not directory_path:
            raise ValueError("Directory path cannot be empty")

        init_file = os.path.join(directory_path, "__init__.py")
        if not os.path.exists(init_file):
            self.stdout.write(f"Creating __init__.py in: {directory_path}")
            with open(init_file, "w") as f:
                f.write("")

    def _ensure_directory_with_init(self, path: str) -> None:
        """Create directory and all parent directories with __init__.py files."""
        if not path:
            raise ValueError("Path cannot be empty")

        current_path = ""
        parts = [p for p in path.split("/") if p]  # Filter out empty strings

        for part in parts:
            current_path = os.path.join(current_path, part) if current_path else part
            self._ensure_directory_exists(current_path)
            self._create_init_file(current_path)

    def _generate_component(self, app_path: str, app_name: str, model_name: str, component: str, fields: list) -> None:
        """Generate files for a specific component."""
        if not app_path:
            raise ValueError("App path cannot be empty")

        config = self.COMPONENT_CONFIGS[component]
        base_path = os.path.join(app_path, config["path"])

        self.stdout.write(f"Generating {component} in {base_path}")

        self._ensure_directory_with_init(app_path)
        self._ensure_directory_with_init(base_path)

        generators = GeneratorFactory.create_generators(
            app_name,
            model_name,
            base_path,
            component
        )
        for generator in generators:
            generator.generate(fields)