from rest_framework import generics, status
from rest_framework.response import Response
from app.models import TestModel
from ...domain.services.test_model import TestModelService
from ...domain.selectors.test_model import TestModelSelector
from .serializers import (
    TestModelMinimalSerializer,
    TestModelDetailedSerializer,
    TestModelCreateSerializer,
    TestModelUpdateSerializer
)
from .filters import TestModelFilter
from .pagination import TestModelPagination

class TestModelListView(generics.ListAPIView):
    serializer_class = TestModelMinimalSerializer
    filterset_class = TestModelFilter
    pagination_class = TestModelPagination

    def get_queryset(self):
        return TestModelSelector.get_queryset()

class TestModelCreateView(generics.CreateAPIView):
    serializer_class = TestModelCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = TestModelService.create_test_model(
            data=serializer.validated_data
        )
        response_serializer = TestModelDetailedSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class TestModelDetailView(generics.RetrieveAPIView):
    serializer_class = TestModelDetailedSerializer
    lookup_field = 'id'

    def get_object(self):
        return TestModelSelector.by_id(id=self.kwargs['id'])

class TestModelUpdateView(generics.UpdateAPIView):
    serializer_class = TestModelUpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        return TestModelSelector.by_id(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        updated_instance = TestModelService.update_test_model(
            instance=instance,
            data=serializer.validated_data
        )
        response_serializer = TestModelDetailedSerializer(updated_instance)
        return Response(response_serializer.data)

class TestModelDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_object(self):
        return TestModelSelector.by_id(id=self.kwargs['id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        TestModelService.delete_test_model(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
