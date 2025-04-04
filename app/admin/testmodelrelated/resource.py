from import_export import resources

from app.models import TestModelRelated


class TestModelRelatedResource(resources.ModelResource):
    class Meta:
        model = TestModelRelated
        fields = ['test_model', 'name', 'description', 'is_active', 'created_at', 'new_filed']
