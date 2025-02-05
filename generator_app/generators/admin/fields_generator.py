from ..base import BaseGenerator


class FieldsGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        field_lines = [f"    {field.upper()} = \"{field}\"" for field in fields]
        content = [
            f"class {self.model_name_capital}Fields:",
            *field_lines,
            "",
            "    @classmethod",
            "    def get_field_name(cls, model, field):",
            "        return model._meta.get_field(field).name"
        ]
        self.write_file('fields.py', '\n'.join(content))
