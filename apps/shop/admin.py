from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "image",
        "description",
        "price",
        "available",
        "created",
        "updated",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "description", "available"]
    prepopulated_fields = {"slug": ("name",)}
