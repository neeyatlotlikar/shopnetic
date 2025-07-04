from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class Discourse(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="discourses", verbose_name="Item"
    )
    members = models.ManyToManyField(
        User, related_name="discourses", verbose_name="Members"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Discourse"
        verbose_name_plural = "Discourses"
        ordering = ("-updated_at",)

    def __str__(self):
        return f"Discourse on {self.item} by {self.members.all().first()}"


class DiscourseMessage(models.Model):
    discourse = models.ForeignKey(
        Discourse,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Discourse",
    )
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_messages",
        verbose_name="Created By",
    )

    class Meta:
        verbose_name = "Discourse Message"
        verbose_name_plural = "Discourse Messages"
        ordering = ("-created_at",)

    def __str__(self):
        return f"Message by {self.created_by} in {self.discourse}"
