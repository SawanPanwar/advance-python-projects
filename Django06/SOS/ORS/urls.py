from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signUp, name="SIGN_UP"),
    path('login/', views.signIn, name="SIGN_IN"),
    path('welcome/', views.welcome, name="WELCOME"),
    path('logout/', views.destroy, name="LOG_OUT"),
]
