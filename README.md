# Interactive Weather Dashboard

A Streamlit web application that displays live current conditions and a three-day
forecast from WeatherAPI. Users can search by city or ZIP code, switch between
Fahrenheit and Celsius, explore an interactive Plotly chart, and review the
underlying forecast data and generated insights.

## Dataset

The app uses the [WeatherAPI forecast API](https://www.weatherapi.com/docs/) as its
dataset. Each request supplies current conditions plus daily high, average, and low
temperatures, average humidity, and a condition description. Results are cached for
10 minutes to limit repeated API requests.

## Features

- City or ZIP code search
- Fahrenheit/Celsius selector
- Current temperature, humidity, wind, and condition metrics
- Interactive Plotly three-day temperature chart
- Forecast data table and automatically calculated insights
- Friendly handling of empty input, invalid locations, missing credentials, and
  network errors

## Project Structure

```text
weather_dashboard/
├── app.py              # Streamlit application
├── weather_api.py      # WeatherAPI data access and normalization
├── main.py             # Original command-line application
├── menu.py             # CLI menu
├── storage.py          # CLI search-history storage
├── utils.py            # CLI display helpers
├── AGILE.md            # Backlog, sprints, and Agile evidence
├── tests/              # API data-normalization tests
├── requirements.txt    # Python dependencies
└── README.md
```

## Run Locally

1. Clone the repository and enter the project folder:

   ```bash
   git clone https://github.com/VicodesRial/CLI-weather-forecast-dashboard.git
   cd CLI-weather-forecast-dashboard
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate it with `.venv\Scripts\activate`.

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Get a free API key from [WeatherAPI](https://www.weatherapi.com/) and create a
   `.env` file in the project folder:

   ```text
   WEATHER_API_KEY=your_api_key_here
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

Enter a location in the sidebar, select a temperature unit, and choose **Update
dashboard**. Hover over the chart points to inspect individual values.

Run the automated tests with:

```bash
python -m unittest discover -s tests
```

## Deploy on Streamlit Community Cloud

1. Push the project to a public GitHub repository. Do not commit `.env`.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and choose
   **Create app**.
3. Select the repository and branch, and set the main file path to `app.py`.
4. In **Advanced settings > Secrets**, add:

   ```toml
   WEATHER_API_KEY = "your_api_key_here"
   ```

5. Deploy the app, then add the public app URL to this README and the assignment
   submission.

## Agile Process

Development uses a lightweight Scrum approach with a product goal, prioritized user
stories, acceptance criteria, two iterations, a Definition of Done, review, and
retrospective. See [AGILE.md](AGILE.md) for the project-management evidence.

## Deliverable Links

- Streamlit app: add the public Streamlit Community Cloud URL after deployment
- GitHub repository: https://github.com/VicodesRial/CLI-weather-forecast-dashboard

## Original CLI

The original interface remains available with `python main.py`. It uses the same
WeatherAPI integration and local `.env` configuration.

## License

This project is for educational and portfolio purposes.
