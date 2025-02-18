import datetime
from django.core.cache import cache
from celery import shared_task
from .make_request import get_weather
from .models import WeatherSearch

CACHE_TIMEOUT = 600  
@shared_task
def update_weather_cache():
    print("Updating weather cache...")
    cache_keys = [key for key in cache.keys("weather_*")]  
    for cache_key in cache_keys:
        city = cache_key.replace("weather_", "")
        
        response = get_weather(city=city)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "City": city.capitalize(),
                "temperature": data['main']['temp'],
                "weather": data['weather'][0]['description'],
            }

            # Update the cache
            cache.set(cache_key, weather_info, timeout=CACHE_TIMEOUT)
            print(f"Updated weather data for {city}")
        else:
            print(f"Failed to update weather data for {city}")
