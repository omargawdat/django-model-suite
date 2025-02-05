from rest_framework import serializers
from apps.app.models.book import Book

class BookMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (id, )
        read_only = True

class BookDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (id,)
        read_only = True

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ()

class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ()
