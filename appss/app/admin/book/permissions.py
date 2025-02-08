from typing import Optional, Dict
from django.http import HttpRequest
from ...fields.book import BookFields
from ....core.admin import FieldPermissions
from appss.app.models.lol import Book
from .context import BookContextLogic


class BookPermissions:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, book: Optional[Book] = None) -> bool:
        return True

    def has_delete_permission(self, request: HttpRequest, book: Optional[Book] = None) -> bool:
        return False

    def get_field_rules(self, request: HttpRequest, book: Optional[Book] = None) -> Dict:
        context = BookContextLogic(request, book)

        return {
            BookFields.ID: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            BookFields.TITLE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            BookFields.AUTHOR: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            BookFields.PUBLICATION_DATE: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            BookFields.NUM_PAGES: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            ),
            BookFields.IS_BORROWED: FieldPermissions(
                visible=(
                    context.is_superuser
                ),
                editable=(
                ),
            )
        }
