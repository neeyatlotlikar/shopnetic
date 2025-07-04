from django.contrib import admin

from .models import Discourse, DiscourseMessage


@admin.register(Discourse)
class DiscourseAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "created_at", "updated_at")
    search_fields = ("item__name", "members__username")
    list_filter = ("created_at", "updated_at")


@admin.register(DiscourseMessage)
class DiscourseMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "discourse", "created_by", "created_at")
    search_fields = ("discourse__item__name", "created_by__username", "content")
    list_filter = ("created_at", "discourse__item")
