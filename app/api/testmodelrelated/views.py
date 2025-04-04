from rest_framework import generics, status
from rest_framework.response import Response
from app.models import TestModelRelated
from ...domain.services.test_model_related import TestModelRelatedService
from ...domain.selectors.test_model_related import TestModelRelatedSelector
from .serializers import (
    TestModelRelatedMinimalSerializer,
    TestModelRelatedDetailedSerializer,
    TestModelRelatedCreateSerializer,
    TestModelRelatedUpdateSerializer
)
from .filters import TestModelRelatedFilter
from .pagination import TestModelRelatedPagination

class TestModelRelatedListView(generics.ListAPIView):
    serializer_class = TestModelRelatedMinimalSerializer
    filterset_class = TestModelRelatedFilter
    pagination_class = TestModelRelatedPagination

    def get_queryset(self):
        return TestModelRelatedSelector.get_queryset()

class TestModelRelatedCreateView(generics.CreateAPIView):
    serializer_class = TestModelRelatedCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = TestModelRelatedService.create_test_model_related(
            data=serializer.validated_data
        )
        response_serializer = TestModelRelatedDetailedSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class TestModelRelatedDetailView(generics.RetrieveAPIView):
    serializer_class = TestModelRelatedDetailedSerializer
    lookup_field = 'id'

    def get_object(self):
        return TestModelRelatedSelector.by_id(id=self.kwargs['id'])

class TestModelRelatedUpdateView(generics.UpdateAPIView):
    serializer_class = TestModelRelatedUpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        return TestModelRelatedSelector.by_id(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        updated_instance = TestModelRelatedService.update_test_model_related(
            instance=instance,
            data=serializer.validated_data
        )
        response_serializer = TestModelRelatedDetailedSerializer(updated_instance)
        return Response(response_serializer.data)

class TestModelRelatedDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_object(self):
        return TestModelRelatedSelector.by_id(id=self.kwargs['id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        TestModelRelatedService.delete_test_model_related(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
