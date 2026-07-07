# Weather Dashboard

A command-line weather application built with Python that allows users to check the current weather, view a 3-day forecast, and store a search history using the WeatherAPI service.

## Features

* 🌤️ View current weather for any city
* 📅 View a 3-day weather forecast
* 📝 Save searched cities to a local history file
* 🗑️ Clear search history
* ⚠️ Handles invalid city names and network errors
* 🔐 Secure API key management using environment variables

## Technologies Used

* Python 3
* Requests
* python-dotenv
* WeatherAPI
* JSON

## Project Structure

```
weather_dashboard/
│── main.py
│── weather.py
│── menu.py
│── storage.py
│── utils.py
│── history.json
│── .env
│── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/VicodesRial/weather_dashboard.git
cd weather_dashboard
```

2. Create and activate a virtual environment:

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder:

```
WEATHER_API_KEY=your_api_key_here
```

You can get a free API key from https://www.weatherapi.com/.

## Running the Project

Run the application with:

```bash
python main.py
```

## Example Menu

```
========== Weather Dashboard ==========
1. Current Weather
2. 3-Day Forecast
3. Search History
4. Clear Search History
5. Exit
=======================================
```

## What I Learned

This project helped me practice:

* Working with REST APIs
* Parsing JSON responses
* Organizing a Python project into multiple modules
* File handling with JSON
* Exception handling
* Using environment variables to protect API keys
* Building interactive command-line applications

## Future Improvements

* 7-day forecast support
* Search history timestamps
* Weather icons in the terminal
* Unit conversion (°F / °C)
* Colorized terminal output
* Export search history to CSV

## License

This project is for educational and portfolio purposes.