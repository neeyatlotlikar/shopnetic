from django.urls import path

from .views import detail

app_name = "items"

urlpatterns = [
    path("<int:item_id>/", detail, name="item_detail"),
]
