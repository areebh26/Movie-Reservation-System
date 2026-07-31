from django.urls import path
from .views import UserLoginView,UserRegistrationView,LogoutView,UpdateUserView,UpdateProfilePicView
from rest_framework_simplejwt.views import  TokenRefreshView



urlpatterns = [
    path("login/" , UserLoginView.as_view() ),
    path("register/",UserRegistrationView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
    path("logout/",LogoutView.as_view()),
    path("update-user/<uuid:id>/",UpdateUserView.as_view()),
    path("update-profile-pic/<uuid:id>/",UpdateProfilePicView.as_view()),
    
]