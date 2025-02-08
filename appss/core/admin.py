from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from typing import Union

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget


@dataclass
class FieldPermissions:
    visible: Union[bool, tuple] = False
    editable: Union[bool, tuple] = False


class DynamicAdminFields(ABC):
    @abstractmethod
    def get_field_rules(self, request, obj=None) -> dict[str, FieldPermissions]:
        """Must be implemented by child classes to define field rules"""

    def get_fieldsets(self, request, obj=None):
        field_rules = self.get_field_rules(request, obj)
        base_fieldsets = super().get_fieldsets(request, obj)

        if not base_fieldsets:
            all_fields = self.get_fields(request, obj)
            visible_fields = [
                field for field in all_fields if field_rules.get(field, FieldPermissions()).visible
            ]
            return ((None, {"fields": visible_fields}),) if visible_fields else ()

        filtered_fieldsets = []
        for name, options in base_fieldsets:
            if not isinstance(options, dict) or "fields" not in options:
                continue

            visible_fields = [
                field
                for field in options["fields"]
                if field_rules.get(field, FieldPermissions()).visible
            ]

            if visible_fields:
                new_options = options.copy()
                new_options["fields"] = visible_fields
                filtered_fieldsets.append((name, new_options))

        return tuple(filtered_fieldsets)

    def get_readonly_fields(self, request, obj=None):
        field_rules = self.get_field_rules(request, obj)
        base_readonly = super().get_readonly_fields(request, obj)

        readonly_fields = list(base_readonly)
        for field, permissions in field_rules.items():
            if permissions.visible and not permissions.editable:
                readonly_fields.append(field)

        return tuple(readonly_fields)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        field_rules = self.get_field_rules(request, obj)

        for field in list(form.base_fields):
            if not field_rules.get(field, FieldPermissions()).visible:
                del form.base_fields[field]

        return form


class BaseModelAdminMeta(ModelAdmin.__class__, ABCMeta):
    pass


class BaseModelAdmin(
    DynamicAdminFields,
    UnfoldModelAdmin,
    ABC,
    metaclass=BaseModelAdminMeta,
):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.filter_horizontal = [field.name for field in model._meta.many_to_many]

    empty_value_display = "-"
    show_facets = admin.ShowFacets.ALWAYS
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }
    compressed_fields = True
    warn_unsaved_form = True

    @abstractmethod
    def has_add_permission(self, request):
        pass

    @abstractmethod
    def has_change_permission(self, request, obj=None):
        pass

    @abstractmethod
    def has_delete_permission(self, request, obj=None):
        pass
