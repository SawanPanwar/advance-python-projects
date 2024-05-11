from django.urls import path
from . import views

urlpatterns = [
    path('api/marksheets/add/', views.add_marksheet),
    path('api/marksheets/<int:pk>/update/', views.update_marksheet),
    path('api/marksheets/get/', views.get_marksheets),
    path('api/marksheets/<int:pk>/delete/', views.delete_marksheet),
]
