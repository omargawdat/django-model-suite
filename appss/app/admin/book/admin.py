from django.contrib import admin
from unfold.admin import ModelAdmin
from .list_view import BookListView
from .change_view import BookChangeView
from .permissions import BookPermissions
from .display import BookDisplayMixin
from appss.app.models.lol import Book
from ....core.admin import BaseModelAdmin

@admin.register(Book)
class BookAdmin(
    BookDisplayMixin,
    BookListView,
    BookChangeView,
    BookPermissions,
    BaseModelAdmin,
):
    pass
