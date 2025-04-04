from django.db.models import QuerySet
from app.models import TestModelRelated

class TestModelRelatedSelector:
    @staticmethod
    def get_queryset() -> QuerySet:
        return TestModelRelated.objects.all()

    @staticmethod
    def by_id(*, id: int) -> TestModelRelated:
        return TestModelRelatedSelector.get_queryset().get(id=id)
