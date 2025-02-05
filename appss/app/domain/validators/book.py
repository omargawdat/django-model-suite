from typing import Any
from django.core.exceptions import ValidationError
from Book import Book

def validate_book_create(*, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data

def validate_book_update(*, instance: Book, data: dict[str, Any]) -> dict[str, Any]:
    # Add your validation logic here
    return data
