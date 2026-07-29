from django.urls import path
from .views import UserLoginView,UserRegistrationView,LogoutView
from rest_framework_simplejwt.views import  TokenRefreshView



urlpatterns = [
    path("login/" , UserLoginView.as_view() ),
    path("register/",UserRegistrationView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
    path("logout/",LogoutView.as_view()),  
]