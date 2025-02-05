from typing import Any
from Book import Book

class BookService:
    @staticmethod
    def create_book(*, data: dict[str, Any]) -> Book:
        validated_data = validate_book_create(data=data)
        instance = Book.objects.create(**validated_data)
        return instance

    @staticmethod
    def update_book(*, instance: Book, data: dict[str, Any]) -> Book:
        validated_data = validate_book_update(instance=instance, data=data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete_book(*, instance: Book) -> None:
        instance.delete()
