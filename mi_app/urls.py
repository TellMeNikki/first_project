from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("fotos", views.fotos),
    path("time_display", views.time_display),
    path("login/<name>", views.login),
    path("logout", views.logout),
]
