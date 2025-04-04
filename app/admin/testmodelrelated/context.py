from typing import Optional
from django.http import HttpRequest
from app.models import TestModelRelated


class TestModelRelatedContextLogic:
    def __init__(self, request: HttpRequest, test_model_related: Optional[TestModelRelated] = None):
        self.request = request
        self.test_model_related = test_model_related

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.test_model_related is None
