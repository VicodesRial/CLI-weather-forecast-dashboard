import json
import os

HISTORY_FILE = "history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r', encoding="utf-8") as f:
        history = json.load(f)
        return history
    
def save_history(history):
    with open(HISTORY_FILE, 'w', encoding="utf-8") as f:
        json.dump(history, f, indent=4)
    
def add_to_history(city):
    history = load_history()
    history.append(city)
    save_history(history)

def view_history():
    history = load_history()
    if not history:
        print("No search history found.")
    
    for index, city in enumerate(history, start=1):
        print(f"{index}. {city}")
def clear_history():
    save_history([])
    print("Search history cleared.")
