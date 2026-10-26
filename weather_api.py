import os
from dotenv import load_dotenv
import requests


load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1"


def _api_key(override=None):
    return override or os.getenv("WEATHER_API_KEY")


def _get(endpoint, city, key=None, **params):
    api_key = _api_key(key)
    if not api_key:
        raise ValueError("WEATHER_API_KEY is not configured.")

    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        params={"key": api_key, "q": city, **params},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_current_weather(city, key=None):
    try:
        data = _get("current.json", city, key)
        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_f"],
            "feels_like": data["current"]["feelslike_f"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_mph"],
            "condition": data["current"]["condition"]["text"],
        }
    except (requests.RequestException, KeyError, ValueError):
        return None


def get_forecast_data(city, days=3, key=None):
    """Return normalized forecast rows for display or visualization."""
    try:
        data = _get("forecast.json", city, key, days=days)
        return [
            {
                "date": day["date"],
                "max_temp_f": day["day"]["maxtemp_f"],
                "min_temp_f": day["day"]["mintemp_f"],
                "avg_temp_f": day["day"]["avgtemp_f"],
                "humidity": day["day"]["avghumidity"],
                "condition": day["day"]["condition"]["text"],
            }
            for day in data["forecast"]["forecastday"]
        ]
    except (requests.RequestException, KeyError, ValueError):
        return None


def get_forecast(city):
    """Display the 3-day forecast for the existing command-line app."""
    forecast = get_forecast_data(city)
    if not forecast:
        return None

    print("========== 3-Day Forecast ==========")
    for day in forecast:
        print(f"Date     : {day['date']}")
        print(f"Max. Temp: {day['max_temp_f']}°F")
        print(f"Min. Temp: {day['min_temp_f']}°F")
        print(f"Condition: {day['condition']}")
        print()
        print("---------------------------------------")
    return forecast
