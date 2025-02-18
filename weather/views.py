import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import WeatherSerializer, WeatherSearchSerializer

from .models import WeatherSearch
from .make_request import get_weather

class WeatherView(APIView):

    def get(self,request):
        serializer = WeatherSerializer(data=request.query_params)
        if serializer.is_valid():
            city = serializer.validated_data['city']
            response = get_weather(city=city)
            if response.status_code == 200:
                data = response.json()

                weather_info = {
                "City":city,
                "temperature" : data['main']['temp'],
                'weather' : data['weather'][0]['description'],
                }
                WeatherSearch.objects.create(city_name=city,timestamp=datetime.datetime.now)
                return Response(weather_info,status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid city or API error"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SerachHistoryView(APIView):
    def get(self,request):
        searches = WeatherSearch.objects.all().order_by("-timestamp")
        serializer = WeatherSearchSerializer(searches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)