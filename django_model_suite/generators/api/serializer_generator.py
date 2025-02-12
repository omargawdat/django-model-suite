# serializer_generator.py
from django_model_suite.generators.base import BaseGenerator

class SerializerGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        content = f"""from rest_framework import serializers
from {model_import_path} import {model_name}

class {model_name}MinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = (id, )
        read_only = True

class {model_name}DetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = (id,)
        read_only = True

class {model_name}CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = ()

class {model_name}UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = ()
"""
        self.write_file("serializers.py", content)