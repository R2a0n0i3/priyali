from DeliciousApp import views
from django.urls import path

urlpatterns = [
    path("login/", views.login, name="login"),
    path("my_views/", views.my_view, name="views"),
]