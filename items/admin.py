from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_by", "is_sold", "created_at")
    list_filter = ("category", "created_by", "is_sold")
    search_fields = ("name", "description")
