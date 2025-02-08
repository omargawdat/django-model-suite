# serializer_generator.py
from django.apps import apps

from django_model_suite.generators.base import BaseGenerator


class SerializerGenerator(BaseGenerator):
    def __init__(self, app_name: str, model_name: str, base_path: str):
        super().__init__(app_name, model_name, base_path)
        self.model = apps.get_model(app_label=self.app_name, model_name=self.model_name)

    def generate(self, fields: list) -> None:
        model_import_path = f"{self.model.__module__}"
        content = f"""from rest_framework import serializers
from {model_import_path} import {self.model_name_capital}

class {self.model_name_capital}MinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = {self.model_name_capital}
        fields = (id, )
        read_only = True

class {self.model_name_capital}DetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = {self.model_name_capital}
        fields = (id,)
        read_only = True

class {self.model_name_capital}CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {self.model_name_capital}
        fields = ()

class {self.model_name_capital}UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {self.model_name_capital}
        fields = ()
"""
        self.write_file("serializers.py", content)