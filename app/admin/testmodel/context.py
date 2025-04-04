from typing import Optional
from django.http import HttpRequest
from app.models import TestModel


class TestModelContextLogic:
    def __init__(self, request: HttpRequest, test_model: Optional[TestModel] = None):
        self.request = request
        self.test_model = test_model

    @property
    def is_superuser(self) -> bool:
        return self.request.user.is_superuser

    @property
    def is_staff(self) -> bool:
        return self.request.user.is_staff

    @property
    def is_creating(self) -> bool:
        return self.test_model is None
