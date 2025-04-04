from rest_framework import serializers
from app.models import TestModel

class TestModelMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = (id, )
        read_only = True

class TestModelDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = (id,)
        read_only = True

class TestModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ()

class TestModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ()
