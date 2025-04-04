from unfold.decorators import display
from app.models import TestModelRelated

class TestModelRelatedDisplayMixin:
    @display(description="test_model_related", header=True)
    def display_header(self, test_model_related: TestModelRelated):
        """Display header with image if available."""
        return [
            test_model_related.pk,
            "",
            "O",
            {"path": test_model_related.image.url if hasattr(test_model_related, 'image') and test_model_related.image else None},
        ]
