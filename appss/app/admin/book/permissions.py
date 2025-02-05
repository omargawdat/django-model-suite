from dataclasses import dataclass

@dataclass
class FieldPermissions:
    visible: bool = False
    editable: bool = False

from .fields import BookFields

class BookPermissions:
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_field_rules(self, request, obj=None):
        is_superuser = request.user.is_superuser
        return {
            BookFields.ID: FieldPermissions(
                visible=False,
                editable=False,
            ),            BookFields.TITLE: FieldPermissions(
                visible=False,
                editable=False,
            ),            BookFields.AUTHOR: FieldPermissions(
                visible=False,
                editable=False,
            ),            BookFields.PUBLICATION_DATE: FieldPermissions(
                visible=False,
                editable=False,
            ),            BookFields.NUM_PAGES: FieldPermissions(
                visible=False,
                editable=False,
            ),            BookFields.IS_BORROWED: FieldPermissions(
                visible=False,
                editable=False,
            )
        }
