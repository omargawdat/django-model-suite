from django_model_suite.generators.base import BaseGenerator

class FieldsGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        field_lines = [f"    {field.upper()} = \"{field}\"" for field in fields]
        content = [
            f"class {model_name}Fields:",
            *field_lines,
            "",
            "    @classmethod",
            "    def get_field_name(cls, model, field):",
            "        return model._meta.get_field(field).name"
        ]
        self.write_file(f'{self.model_name_lower}.py', '\n'.join(content))