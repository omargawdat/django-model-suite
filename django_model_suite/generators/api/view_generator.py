from django_model_suite.generators.base import BaseGenerator


class ViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        model_import_path = f"{self.model.__module__}"
        content = f'''from rest_framework import generics, status
from rest_framework.response import Response
from {model_import_path} import {model_name}
from ...domain.services.{self.model_name_lower} import {model_name}Service
from ...domain.selectors.{self.model_name_lower} import {model_name}Selector
from .serializers import (
    {model_name}MinimalSerializer,
    {model_name}DetailedSerializer,
    {model_name}CreateSerializer,
    {model_name}UpdateSerializer
)
from .filters import {model_name}Filter
from .pagination import {model_name}Pagination

class {model_name}ListView(generics.ListAPIView):
    serializer_class = {model_name}MinimalSerializer
    filterset_class = {model_name}Filter
    pagination_class = {model_name}Pagination

    def get_queryset(self):
        return {model_name}Selector.get_queryset()

class {model_name}CreateView(generics.CreateAPIView):
    serializer_class = {model_name}CreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = {model_name}Service.create_{self.model_name_lower}(
            data=serializer.validated_data
        )
        response_serializer = {model_name}DetailedSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class {model_name}DetailView(generics.RetrieveAPIView):
    serializer_class = {model_name}DetailedSerializer
    lookup_field = 'id'

    def get_object(self):
        return {model_name}Selector.by_id(id=self.kwargs['id'])

class {model_name}UpdateView(generics.UpdateAPIView):
    serializer_class = {model_name}UpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        return {model_name}Selector.by_id(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        updated_instance = {model_name}Service.update_{self.model_name_lower}(
            instance=instance,
            data=serializer.validated_data
        )
        response_serializer = {model_name}DetailedSerializer(updated_instance)
        return Response(response_serializer.data)

class {model_name}DeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_object(self):
        return {model_name}Selector.by_id(id=self.kwargs['id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        {model_name}Service.delete_{self.model_name_lower}(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
        self.write_file('views.py', content)
