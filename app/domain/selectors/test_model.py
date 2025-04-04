from django.db.models import QuerySet
from app.models import TestModel

class TestModelSelector:
    @staticmethod
    def get_queryset() -> QuerySet:
        return TestModel.objects.all()

    @staticmethod
    def by_id(*, id: int) -> TestModel:
        return TestModelSelector.get_queryset().get(id=id)
