from generator_app.generators.base import BaseGenerator


class SerializerGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f"""from rest_framework import serializers
from apps.{self.app_name}.models.{self.model_name_lower} import {self.model_name_capital}

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
