from rest_framework import generics, status
from rest_framework.response import Response
from apps.app.models.book import Book
from apps.app.domain.services.book import BookService
from apps.app.domain.selectors.book import BookSelector
from .serializers import (
    BookMinimalSerializer,
    BookDetailedSerializer,
    BookCreateSerializer,
    BookUpdateSerializer
)
from .filters import BookFilter
from .pagination import BookPagination

class BookListView(generics.ListAPIView):
    serializer_class = BookMinimalSerializer
    filterset_class = BookFilter
    pagination_class = BookPagination

    def get_queryset(self):
        return BookSelector.get_queryset()

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = BookService.create_book(
            data=serializer.validated_data
        )
        response_serializer = BookDetailedSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class BookDetailView(generics.RetrieveAPIView):
    serializer_class = BookDetailedSerializer
    lookup_field = 'id'

    def get_object(self):
        return BookSelector.by_id(id=self.kwargs['id'])

class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookUpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        return BookSelector.by_id(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        updated_instance = BookService.update_book(
            instance=instance,
            data=serializer.validated_data
        )
        response_serializer = BookDetailedSerializer(updated_instance)
        return Response(response_serializer.data)

class BookDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_object(self):
        return BookSelector.by_id(id=self.kwargs['id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        BookService.delete_book(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
