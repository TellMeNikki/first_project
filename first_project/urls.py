from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include

urlpatterns = [
    path("", include("mi_app.urls")),
    path("admin/", admin.site.urls),
]
