from typing import Optional
from django.http import HttpRequest
from appss.app.models.lol import Book


class BookContextLogic:
    def __init__(self, request: HttpRequest, book: Optional[Book] = None):
        self.request = request
        self.book = book

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.book is None
