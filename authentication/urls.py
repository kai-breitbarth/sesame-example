from django.urls import path
from sesame.views import LoginView
from . import views

urlpatterns = [
    path("", views.email_login_view, name="email_login"),
    path("auth/", LoginView.as_view(), name="login"),
]
