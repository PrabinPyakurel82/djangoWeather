from rest_framework import serializers

from .models import WeatherSearch

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)

class WeatherSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherSearch
        fields = ['city_name','timestamp']