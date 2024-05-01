from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("add/", views.add_user),
    path("get/", views.getAllUser),
    path("update/", views.update_user),
    path("delete/", views.delete_user),
]
