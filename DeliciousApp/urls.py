from DeliciousApp import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("my_views/", views.my_view, name="views"),
]