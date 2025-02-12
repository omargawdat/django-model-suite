# url_generator.py
from django_model_suite.generators.base import BaseGenerator

class URLGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        model_name = self.model.__name__
        content = f"""from django.urls import path
from .views import (
    {model_name}ListView,
    {model_name}CreateView,
    {model_name}DetailView,
    {model_name}UpdateView,
    {model_name}DeleteView
)

urlpatterns = [
    path('{self.model_name_lower}s/', {model_name}ListView.as_view(), name='{self.model_name_lower}-list'),
    path('{self.model_name_lower}/create/', {model_name}CreateView.as_view(), name='{self.model_name_lower}-create'),
    path('{self.model_name_lower}/<int:id>/', {model_name}DetailView.as_view(), name='{self.model_name_lower}-detail'),
    path('{self.model_name_lower}/<int:id>/update/', {model_name}UpdateView.as_view(), name='{self.model_name_lower}-update'),
    path('{self.model_name_lower}/<int:id>/delete/', {model_name}DeleteView.as_view(), name='{self.model_name_lower}-delete'),
]
"""
        self.write_file("urls.py", content)