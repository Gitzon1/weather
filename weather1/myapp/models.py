from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    weather_icon = models.CharField(max_length=100)
