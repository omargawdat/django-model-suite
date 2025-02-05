from django.contrib import admin
from unfold.admin import ModelAdmin
# from common.base.basemodeladmin import BaseModelAdmin  # Uncomment if using BaseModelAdmin
from .list_view import BookListView
from .change_view import BookChangeView
from .permissions import BookPermissions
from .display import BookDisplayMixin
from .fields import BookFields
from appss.app.models.lol import Book

@admin.register(Book)
class BookAdmin(
    ModelAdmin,  # Change to BaseModelAdmin if using base model admin
    BookDisplayMixin,
    BookListView,
    BookChangeView,
    BookPermissions
):
    pass
