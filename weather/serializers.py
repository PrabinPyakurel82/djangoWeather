from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)