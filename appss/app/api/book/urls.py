from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:id>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
