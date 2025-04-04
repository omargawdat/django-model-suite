from import_export import resources

from app.models import TestModel


class TestModelResource(resources.ModelResource):
    class Meta:
        model = TestModel
        fields = ['name']
