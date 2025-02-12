from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100)


class TestModelRelated(models.Model):
    test_model = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

