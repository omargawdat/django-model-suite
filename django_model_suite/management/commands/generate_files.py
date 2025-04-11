import os

from django.apps import apps
from django.core.management import BaseCommand

from ...generators.admin.admin_generator import AdminGenerator
from ...generators.admin.change_view_generator import ChangeViewGenerator
from ...generators.admin.context_generator import ContextGenerator
from ...generators.admin.display_generator import DisplayGenerator
from ...generators.admin.inline import InlineAdminGenerator
from ...generators.admin.list_view_generator import ListViewGenerator
from ...generators.admin.permissions_generator import PermissionsGenerator
from ...generators.admin.resource_generator import ResourceGenerator
from ...generators.api.filter_generator import FilterGenerator
from ...generators.api.pagination_generator import PaginationGenerator
from ...generators.api.serializer_generator import SerializerGenerator
from ...generators.api.url_generator import URLGenerator
from ...generators.api.view_generator import ViewGenerator
from ...generators.domain.selector_generator import SelectorGenerator
from ...generators.domain.service_generator import ServiceGenerator
from ...generators.domain.validator_generator import ValidatorGenerator
from ...generators.field.fields_generator import FieldsGenerator
from ...generators.model_utils import get_model_fields


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
                # ContextGenerator,
                DisplayGenerator,
                ResourceGenerator,
                InlineAdminGenerator,
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
                        app_path, app_name, model_name, component, config, fields, options
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
            options: dict,
    ) -> None:
        path_template = config["path_template"].format(model=model_name.lower())
        base_path = os.path.join(app_path, path_template)
        self.stdout.write(f"Generating {component} in {base_path}")

        model_class = apps.get_model(app_name, model_name)

        # Generate admin classes
        generators = [
            generator_class(app_name, model_name, base_path, model_class)
            for generator_class in config["generators"]
        ]

        # Track if inline was generated to update admin generator
        has_generated_inline = False
        
        for generator in generators:
            if isinstance(generator, InlineAdminGenerator):
                generator.generate(fields=fields)
                has_generated_inline = True
            elif isinstance(generator, AdminGenerator) and has_generated_inline:
                # If inline was generated, tell admin generator to include it
                generator.generate(fields=fields, has_inline=True)
            else:
                generator.generate(fields)
