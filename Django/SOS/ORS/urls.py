from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Hello/', views.hello),
    path('User/', views.user),
    path('User/<int:id>', views.user),
    path('User/<str:name>', views.user),
    path('User/<int:id>/<str:name>', views.user),
    path('Welcome/', views.welcome),
    path('Reg/', views.registration),
    path('List/', views.list),
    path('search/', views.search),
    path('test/', views.test),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('set/', views.setCookies),
    path('get/', views.getCookies),
    path('red/', views.testRedirect),
]
