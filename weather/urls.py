from django.urls import path
from .views import WeatherView,SearchHistoryView

urlpatterns = [
    path("weather/",WeatherView.as_view(),name='weather'),
    path("history/",SearchHistoryView.as_view(),name='history')
]