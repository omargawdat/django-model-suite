import os

from django.apps import apps
from django.core.management import BaseCommand

from generator_app.generators.admin.admin_generator import AdminGenerator
from generator_app.generators.admin.change_view_generator import ChangeViewGenerator
from generator_app.generators.admin.display_generator import DisplayGenerator
from generator_app.generators.admin.fields_generator import FieldsGenerator
from generator_app.generators.admin.list_view_generator import ListViewGenerator
from generator_app.generators.admin.permissions_generator import PermissionsGenerator
from generator_app.generators.api.filter_generator import FilterGenerator
from generator_app.generators.api.pagination_generator import PaginationGenerator
from generator_app.generators.api.serializer_generator import SerializerGenerator
from generator_app.generators.api.url_generator import URLGenerator
from generator_app.generators.api.view_generator import ViewGenerator
from generator_app.generators.domain.selector_generator import SelectorGenerator
from generator_app.generators.domain.service_generator import ServiceGenerator
from generator_app.generators.domain.validator_generator import ValidatorGenerator
from generator_app.generators.model_utils import get_model_fields


class Command(BaseCommand):
    COMPONENT_CONFIGS = {
        "admin": {
            "path_template": "admin/{model}/",  # Will generate admin/user/
            "generators": [
                FieldsGenerator,
                ListViewGenerator,
                ChangeViewGenerator,
                PermissionsGenerator,
                DisplayGenerator,
                AdminGenerator,
            ],
        },
        "api": {
            "path_template": "api/{model}/",
            "generators": [
                SerializerGenerator,
                ViewGenerator,
                URLGenerator,
                FilterGenerator,
                PaginationGenerator,
            ],
        },
        "selectors": {
            "path_template": "domain/selectors/",
            "generators": [SelectorGenerator],
        },
        "services": {
            "path_template": "domain/services/",
            "generators": [ServiceGenerator],
        },
        "validators": {
            "path_template": "domain/validators/",
            "generators": [ValidatorGenerator],
        },
    }

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="Name of the app (e.g., user)")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def get_app_path(self, app_name: str) -> str:
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

            for component, config in self.COMPONENT_CONFIGS.items():
                self._generate_component(
                    app_path, app_name, model_name, component, config, fields
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully generated files for model '{model_name}'")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

    def _generate_component(
            self,
            app_path: str,
            app_name: str,
            model_name: str,
            component: str,
            config: dict,
            fields: list,
    ) -> None:
        path_template = config["path_template"].format(model=model_name.lower())
        base_path = os.path.join(app_path, path_template)
        self.stdout.write(f"Generating {component} in {base_path}")

        generators = [
            generator_class(app_name, model_name, base_path)
            for generator_class in config["generators"]
        ]

        for generator in generators:
            generator.generate(fields)
