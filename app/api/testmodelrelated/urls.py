from django.urls import path
from .views import (
    TestModelRelatedListView,
    TestModelRelatedCreateView,
    TestModelRelatedDetailView,
    TestModelRelatedUpdateView,
    TestModelRelatedDeleteView
)

urlpatterns = [
    path('test_model_relateds/', TestModelRelatedListView.as_view(), name='test_model_related-list'),
    path('test_model_related/create/', TestModelRelatedCreateView.as_view(), name='test_model_related-create'),
    path('test_model_related/<int:id>/', TestModelRelatedDetailView.as_view(), name='test_model_related-detail'),
    path('test_model_related/<int:id>/update/', TestModelRelatedUpdateView.as_view(), name='test_model_related-update'),
    path('test_model_related/<int:id>/delete/', TestModelRelatedDeleteView.as_view(), name='test_model_related-delete'),
]
