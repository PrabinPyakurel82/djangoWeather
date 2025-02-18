from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch



class WeatherViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/weather/"
        self.valid_city = "London"
        self.invalid_city = "InvalidCity"

    @patch("weather.make_request.get_weather")  
    def test_get_weather_valid_city(self, mock_get_weather):
        
        mock_get_weather.return_value.status_code = 200
        
        response = self.client.get(self.url, {"city": self.valid_city})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    @patch("weather.make_request.get_weather")
    def test_get_weather_invalid_city(self, mock_get_weather):
        mock_get_weather.return_value.status_code = 404
        mock_get_weather.return_value.json.return_value = {
            "cod": "404",
            "message": "city not found",
        }

        
        response = self.client.get(self.url, {"city": self.invalid_city})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())

