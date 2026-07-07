from menu import show_menu
from utils import pause, clear_console, display_weather
from weather_api import get_current_weather, get_forecast
from storage import add_to_history, view_history, clear_history, load_history

load_history()
try:
    while True:
        clear_console()

        choice = show_menu()
        
        if choice == 1:
            city = input("Enter City: ")
            weather = get_current_weather(city)
            if weather:
                display_weather(weather)
                add_to_history(city)
            pause()
        elif choice == 2:
            city = input("Enter City: ")
            get_forecast(city)
            pause()
        elif choice == 3:
            view_history()
            pause()
        elif choice == 4:
            clear_history()
            pause()
        elif choice == 5:
            print("")
            print("====================================")
            print("")
            print("Goodbye!")
            break
except KeyboardInterrupt:
    print("\nProgram closed.")