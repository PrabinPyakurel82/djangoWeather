import requests
from django.conf import settings

def get_weather(city):
    api_key = settings.API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    return requests.get(url)
