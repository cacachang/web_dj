from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("chats/", include("chats.urls")),
    path("admin/", admin.site.urls),
]
