import os
from datetime import datetime

def get_current_date():
    auto_date = datetime.now().strftime("%Y-%m-%d")
    return auto_date

def clear_console():
    if os.name == "nt":      
        os.system("cls")
    else:                    
        os.system("clear")

def pause():
    input("\nPress Enter to continue...")

def display_weather(weather):
    print("========== Current Weather ==========")
    print()
    print(f"City        : {weather['city']}")
    print(f"Region      : {weather['region']}")
    print(f"Country     : {weather['country']}")
    print()
    print(f"Temperature : {weather['temperature']}°F")
    print(f"Feels Like  : {weather['feels_like']}°F")
    print(f"Condition   : {weather['condition']}")
    print(f"Humidity    : {weather['humidity']}%")
    print(f"Wind Speed  : {weather['wind_speed']} mph")
    print("====================================")