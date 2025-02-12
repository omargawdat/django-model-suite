from django.contrib import admin
from unfold.admin import ModelAdmin

from app.models import TestModel


@admin.register(TestModel)
class AuthorAdmin(ModelAdmin):
    list_display = ('name',)

#
# @admin.register(TestModelRelated)
# class TestModelRelatedAdmin(ModelAdmin):
#     list_display = ('test_model', 'name')
