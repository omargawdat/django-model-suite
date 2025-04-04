from django.db import models
from django.utils import timezone


class TestModel(models.Model):
    name = models.CharField(max_length=100)

class TestModelRelated(models.Model):
    test_model = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    new_filed = models.CharField(max_length=100, default="default_value")

class UnRelatedModel(models.Model):
    name = models.CharField(max_length=100)
    test_model = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    test_model_related = models.ForeignKey(TestModelRelated, on_delete=models.CASCADE)
