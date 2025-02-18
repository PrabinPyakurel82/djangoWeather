from django.urls import path
from .views import WeatherView,SerachHistoryView
urlpatterns = [
    path("weather/",WeatherView.as_view(),name='weather'),
    path("history/",SerachHistoryView.as_view(),name='history')
]