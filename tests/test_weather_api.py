import unittest
from unittest.mock import Mock, patch

import requests

from weather_api import get_current_weather, get_forecast_data


class WeatherApiTests(unittest.TestCase):
    @patch("weather_api.requests.get")
    def test_current_weather_is_normalized(self, request):
        response = Mock()
        response.json.return_value = {
            "location": {
                "name": "Test City",
                "region": "Test Region",
                "country": "Test Country",
            },
            "current": {
                "temp_f": 68,
                "feelslike_f": 67,
                "humidity": 50,
                "wind_mph": 5,
                "condition": {"text": "Clear"},
            },
        }
        request.return_value = response

        weather = get_current_weather("Test City", key="test-key")

        self.assertEqual(weather["city"], "Test City")
        self.assertEqual(weather["temperature"], 68)
        request.assert_called_once_with(
            "https://api.weatherapi.com/v1/current.json",
            params={"key": "test-key", "q": "Test City"},
            timeout=10,
        )

    @patch("weather_api.requests.get")
    def test_forecast_is_normalized(self, request):
        response = Mock()
        response.json.return_value = {
            "forecast": {
                "forecastday": [
                    {
                        "date": "2026-10-26",
                        "day": {
                            "maxtemp_f": 70,
                            "mintemp_f": 50,
                            "avgtemp_f": 60,
                            "avghumidity": 55,
                            "condition": {"text": "Sunny"},
                        },
                    }
                ]
            }
        }
        request.return_value = response

        forecast = get_forecast_data("Test City", key="test-key")

        self.assertEqual(forecast[0]["avg_temp_f"], 60)
        self.assertEqual(forecast[0]["condition"], "Sunny")

    @patch("weather_api.requests.get", side_effect=requests.RequestException)
    def test_network_error_returns_none(self, _request):
        self.assertIsNone(get_current_weather("Test City", key="test-key"))


if __name__ == "__main__":
    unittest.main()
