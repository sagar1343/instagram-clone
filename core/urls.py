from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_user, name="register-user"),
    path("login/", views.login_user, name="login-user"),
    path("logout/", views.logout_user, name="logout-user"),
    path("profile/", views.profile, name="profile"),
    path("posts/", views.create_post, name="create-post"),
    path("posts/<int:id>/like", views.like_post, name="like-post"),
    path("profile/<str:username>/", views.user_profile, name="user-profile"),
    path("profile/<str:username>/follow", views.follow_profile, name="follow-profile"),
]
