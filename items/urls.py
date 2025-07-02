from django.urls import path

from .views import detail, new, delete, edit, items

app_name = "items"

urlpatterns = [
    path("", items, name="item_list"),
    path("new/", new, name="new"),
    path("<int:item_id>/", detail, name="item_detail"),
    path("<int:item_id>/delete/", delete, name="item_delete"),
    path("<int:item_id>/edit/", edit, name="item_edit"),
]
