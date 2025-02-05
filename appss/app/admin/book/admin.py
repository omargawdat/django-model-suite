from django.contrib import admin
from common.base.basemodeladmin import BaseModelAdmin
from .list_view import BookListView
from .change_view import BookChangeView
from .permissions import BookPermissions
from .display import BookDisplayMixin
from .fields import BookFields
from apps.app.models import Book


@admin.register(Book)
class BookAdmin(
    BaseModelAdmin,
    BookDisplayMixin,
    BookListView,
    BookChangeView,
    BookPermissions
):
    pass
