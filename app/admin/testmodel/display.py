from unfold.decorators import display
from app.models import TestModel

class TestModelDisplayMixin:
    @display(description="test_model", header=True)
    def display_header(self, test_model: TestModel):
        """Display header with image if available."""
        return [
            test_model.pk,
            "",
            "O",
            {"path": test_model.image.url if hasattr(test_model, 'image') and test_model.image else None},
        ]
