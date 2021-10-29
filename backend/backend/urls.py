from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("users/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
