from django.urls import path
from .views import (
    TestModelListView,
    TestModelCreateView,
    TestModelDetailView,
    TestModelUpdateView,
    TestModelDeleteView
)

urlpatterns = [
    path('test_models/', TestModelListView.as_view(), name='test_model-list'),
    path('test_model/create/', TestModelCreateView.as_view(), name='test_model-create'),
    path('test_model/<int:id>/', TestModelDetailView.as_view(), name='test_model-detail'),
    path('test_model/<int:id>/update/', TestModelUpdateView.as_view(), name='test_model-update'),
    path('test_model/<int:id>/delete/', TestModelDeleteView.as_view(), name='test_model-delete'),
]
