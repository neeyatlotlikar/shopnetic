from django.urls import path

from .views import new_discourse, inbox, detail

app_name = "discourse"

urlpatterns = [
    path("", inbox, name="inbox"),
    path("detail/<int:discourse_id>/", detail, name="detail"),
    path("new/<int:item_id>/", new_discourse, name="new"),
]
