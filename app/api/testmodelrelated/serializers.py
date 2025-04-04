from rest_framework import serializers
from app.models import TestModelRelated

class TestModelRelatedMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModelRelated
        fields = (id, )
        read_only = True

class TestModelRelatedDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModelRelated
        fields = (id,)
        read_only = True

class TestModelRelatedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModelRelated
        fields = ()

class TestModelRelatedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModelRelated
        fields = ()
