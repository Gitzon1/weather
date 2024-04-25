from django.urls import path
from .views import WeatherViewSet

urlpatterns = [
    path('weather/', WeatherViewSet.as_view({'get': 'list', 'post': 'create'}), name='weather-list'),
    path('weather/<int:pk>/', WeatherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='weather-detail'),
]
