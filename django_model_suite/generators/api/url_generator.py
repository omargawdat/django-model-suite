from django_model_suite.generators.base import BaseGenerator


class URLGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f"""from django.urls import path
from .views import (
    {self.model_name_capital}ListView,
    {self.model_name_capital}CreateView,
    {self.model_name_capital}DetailView,
    {self.model_name_capital}UpdateView,
    {self.model_name_capital}DeleteView
)

urlpatterns = [
    path('{self.model_name_lower}s/', {self.model_name_capital}ListView.as_view(), name='{self.model_name_lower}-list'),
    path('{self.model_name_lower}/create/', {self.model_name_capital}CreateView.as_view(), name='{self.model_name_lower}-create'),
    path('{self.model_name_lower}/<int:id>/', {self.model_name_capital}DetailView.as_view(), name='{self.model_name_lower}-detail'),
    path('{self.model_name_lower}/<int:id>/update/', {self.model_name_capital}UpdateView.as_view(), name='{self.model_name_lower}-update'),
    path('{self.model_name_lower}/<int:id>/delete/', {self.model_name_capital}DeleteView.as_view(), name='{self.model_name_lower}-delete'),
]
"""
        self.write_file("urls.py", content)
