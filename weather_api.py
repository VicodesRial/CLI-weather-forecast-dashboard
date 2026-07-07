import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

def get_current_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Enter a valid city")
            return None
        else: 
            data_dict = response.json()
            data = {
                "city": data_dict['location']['name'],
                "region": data_dict["location"]["region"],
                "country": data_dict['location']['country'],
                "temperature": data_dict["current"]["temp_f"],
                "feels_like": data_dict["current"]["feelslike_f"],
                "humidity": data_dict["current"]["humidity"],
                "wind_speed": data_dict["current"]["wind_mph"],
                "condition": data_dict["current"]["condition"]["text"]
            }

            return data
    except Exception:
        return None

def get_forecast(city):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        else:
            data = response.json()
            print("========== 3-Day Forecast ==========")
            for day in data['forecast']['forecastday']:
                print(f"Date     : {day['date']}")
                print(f"Max. Temp: {day['day']['maxtemp_f']}°F")  
                print(f"Min. Temp: {day['day']['mintemp_f']}°F")  
                print(f"Condition: {day['day']['condition']['text']}")
                print()
                print("---------------------------------------")
    except Exception:
        return None