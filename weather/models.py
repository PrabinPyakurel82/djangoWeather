from django.db import models

# Create your models here.
class WeatherSearch(models.Model):
    city_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name