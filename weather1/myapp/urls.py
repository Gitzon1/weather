from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    path('weather/', WeatherViewSet.as_view(), name='weather-list'),
    path('weather/<int:pk>/', WeatherViewSet.as_view(), name='weather-detail'),
]
