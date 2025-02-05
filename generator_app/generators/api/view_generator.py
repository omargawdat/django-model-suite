from generator_app.generators.base import BaseGenerator


class ViewGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f'''from rest_framework import generics, status
from rest_framework.response import Response
from apps.{self.app_name}.models.{self.model_name_lower} import {self.model_name_capital}
from apps.{self.app_name}.domain.services.{self.model_name_lower} import {self.model_name_capital}Service
from apps.{self.app_name}.domain.selectors.{self.model_name_lower} import {self.model_name_capital}Selector
from .serializers import (
    {self.model_name_capital}MinimalSerializer,
    {self.model_name_capital}DetailedSerializer,
    {self.model_name_capital}CreateSerializer,
    {self.model_name_capital}UpdateSerializer
)
from .filters import {self.model_name_capital}Filter
from .pagination import {self.model_name_capital}Pagination

class {self.model_name_capital}ListView(generics.ListAPIView):
    serializer_class = {self.model_name_capital}MinimalSerializer
    filterset_class = {self.model_name_capital}Filter
    pagination_class = {self.model_name_capital}Pagination

    def get_queryset(self):
        return {self.model_name_capital}Selector.get_queryset()

class {self.model_name_capital}CreateView(generics.CreateAPIView):
    serializer_class = {self.model_name_capital}CreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = {self.model_name_capital}Service.create_{self.model_name_lower}(
            data=serializer.validated_data
        )
        response_serializer = {self.model_name_capital}DetailedSerializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class {self.model_name_capital}DetailView(generics.RetrieveAPIView):
    serializer_class = {self.model_name_capital}DetailedSerializer
    lookup_field = 'id'

    def get_object(self):
        return {self.model_name_capital}Selector.by_id(id=self.kwargs['id'])

class {self.model_name_capital}UpdateView(generics.UpdateAPIView):
    serializer_class = {self.model_name_capital}UpdateSerializer
    lookup_field = 'id'

    def get_object(self):
        return {self.model_name_capital}Selector.by_id(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        updated_instance = {self.model_name_capital}Service.update_{self.model_name_lower}(
            instance=instance,
            data=serializer.validated_data
        )
        response_serializer = {self.model_name_capital}DetailedSerializer(updated_instance)
        return Response(response_serializer.data)

class {self.model_name_capital}DeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_object(self):
        return {self.model_name_capital}Selector.by_id(id=self.kwargs['id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        {self.model_name_capital}Service.delete_{self.model_name_lower}(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
        self.write_file(f'views.py', content)
