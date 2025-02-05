from .admin.admin_generator import AdminGenerator
from .admin.change_view_generator import ChangeViewGenerator
from .admin.display_generator import DisplayGenerator
from .admin.fields_generator import FieldsGenerator
from .admin.list_view_generator import ListViewGenerator
from .admin.permissions_generator import PermissionsGenerator
from .api.filter_generator import FilterGenerator
from .api.pagination_generator import PaginationGenerator
from .api.serializer_generator import SerializerGenerator
from .api.url_generator import URLGenerator
from .api.view_generator import ViewGenerator
from .base import BaseGenerator
from .domain.selector_generator import SelectorGenerator
from .domain.service_generator import ServiceGenerator
from .domain.validator_generator import ValidatorGenerator


class GeneratorFactory:
    GENERATORS = {
        "admin": [
            FieldsGenerator,
            ListViewGenerator,
            ChangeViewGenerator,
            PermissionsGenerator,
            DisplayGenerator,
            AdminGenerator,
        ],
        "api": [
            SerializerGenerator,
            ViewGenerator,
            URLGenerator,
            FilterGenerator,
            PaginationGenerator,
        ],
        "selectors": [SelectorGenerator],
        "services": [ServiceGenerator],
        "validators": [ValidatorGenerator]
    }

    @classmethod
    def create_generators(
        cls, app_name: str, model_name: str, base_path: str, generator_type: str
    ) -> list[BaseGenerator]:
        if generator_type not in cls.GENERATORS:
            raise ValueError(
                f"Invalid generator type. Must be one of: {', '.join(cls.GENERATORS.keys())}"
            )

        return [
            generator_class(app_name, model_name, base_path)
            for generator_class in cls.GENERATORS[generator_type]
        ]
