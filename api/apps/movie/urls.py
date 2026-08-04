from django.urls import path
from .views import GetMoviesView


urlpatterns = [
    path("get-movies/" , GetMoviesView.as_view() ),
    path("get-movies/<uuid:pk>/" , GetMoviesView.as_view() ),
]