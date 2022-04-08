from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)

    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
    )
