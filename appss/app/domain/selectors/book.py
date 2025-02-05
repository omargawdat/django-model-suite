from django.db.models import QuerySet
from appss.app.models.lol import Book

class BookSelector:
    @staticmethod
    def get_queryset() -> QuerySet:
        return Book.objects.all()

    @staticmethod
    def by_id(*, id: int) -> Book:
        return BookSelector.get_queryset().get(id=id)
