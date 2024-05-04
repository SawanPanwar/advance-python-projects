from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('signin/', views.user_signin),
    path('signup/', views.user_register),
    path('add/', views.add_user),
    path('list/', views.user_list),
    path('welcome/', views.welcome),
]
