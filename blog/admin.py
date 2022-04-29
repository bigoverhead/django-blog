from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)

    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Post)
class PostAdmin(MarkdownxModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
    )
