from unfold.decorators import display
from appss.app.models.lol import Book

class BookDisplayMixin:
    @display(description="book", header=True)
    def display_header(self, book: Book):
        """Display header with image if available."""
        return [
            book.pk,
            "",
            "O",
            {"path": book.image.url if hasattr(book, 'image') and book.image else None},
        ]
