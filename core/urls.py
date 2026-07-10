from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_user, name="register-user"),
    path("login/", views.login_user, name="login-user"),
    path("logout/", views.logout_user, name="logout-user"),
    path("profile/", views.profile, name="profile"),
]
