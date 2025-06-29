from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm
from .views import contact, index, signup, logout_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path(
        "login/",
        LoginView.as_view(
            authentication_form=LoginForm, template_name="core/login.html"
        ),
        name="login",
    ),
    path("logout/", logout_view, name="logout"),
    path("contact/", contact, name="contact"),
]
