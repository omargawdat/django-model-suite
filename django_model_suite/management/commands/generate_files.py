import os

from django.apps import apps
from django.core.management import BaseCommand

from django_model_suite.generators.admin.admin_generator import AdminGenerator
from django_model_suite.generators.admin.change_view_generator import ChangeViewGenerator
from django_model_suite.generators.admin.context_generator import ContextGenerator
from django_model_suite.generators.admin.display_generator import DisplayGenerator
from django_model_suite.generators.admin.list_view_generator import ListViewGenerator
from django_model_suite.generators.admin.permissions_generator import PermissionsGenerator
from django_model_suite.generators.api.filter_generator import FilterGenerator
from django_model_suite.generators.api.pagination_generator import PaginationGenerator
from django_model_suite.generators.api.serializer_generator import SerializerGenerator
from django_model_suite.generators.api.url_generator import URLGenerator
from django_model_suite.generators.api.view_generator import ViewGenerator
from django_model_suite.generators.domain.selector_generator import SelectorGenerator
from django_model_suite.generators.domain.service_generator import ServiceGenerator
from django_model_suite.generators.domain.validator_generator import ValidatorGenerator
from django_model_suite.generators.field.fields_generator import FieldsGenerator
from django_model_suite.generators.model_utils import get_model_fields


class Command(BaseCommand):
    COMPONENT_CONFIGS = {
        "fields": {
            "path_template": "fields/",
            "generators": [
                FieldsGenerator,
            ],
        },
        "admin": {
            "path_template": "admin/{model}/",
            "generators": [
                ListViewGenerator,
                ChangeViewGenerator,
                PermissionsGenerator,
                ContextGenerator,
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
        parser.add_argument(
            "--components",
            nargs="+",
            choices=["admin", "domain", "api"] + list(self.COMPONENT_CONFIGS.keys()),
            help="Specify components to generate (e.g., --components admin services). If not specified, all components will be generated.",
        )

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
        selected_components = options.get("components")

        try:
            app_path = self.get_app_path(app_name)
            if not app_path:
                raise ValueError("App path cannot be empty")

            fields = get_model_fields(app_name, model_name)

            if not selected_components:
                components_to_generate = self.COMPONENT_CONFIGS.keys()
            else:
                components_to_generate = []
                if "admin" in selected_components:
                    components_to_generate.extend(["fields", "admin"])
                if "domain" in selected_components:
                    components_to_generate.extend(["selectors", "services", "validators"])
                if "api" in selected_components:
                    components_to_generate.append("api")
                components_to_generate.extend(
                    [comp for comp in selected_components if comp in self.COMPONENT_CONFIGS]
                )

            components_to_generate = list(set(components_to_generate))  # Remove duplicates

            for component in components_to_generate:
                config = self.COMPONENT_CONFIGS.get(component)
                if config:
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

        model_class = apps.get_model(app_name, model_name)

        generators = [
            generator_class(app_name, model_name, base_path, model_class)
            for generator_class in config["generators"]
        ]

        for generator in generators:
            generator.generate(fields)
