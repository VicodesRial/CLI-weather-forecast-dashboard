import os

import pandas as pd
import plotly.express as px
import streamlit as st

from weather_api import get_current_weather, get_forecast_data


st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")


def get_api_key():
    """Read the API key locally or from Streamlit Community Cloud secrets."""
    if os.getenv("WEATHER_API_KEY"):
        return os.getenv("WEATHER_API_KEY")
    try:
        return st.secrets["WEATHER_API_KEY"]
    except (KeyError, FileNotFoundError):
        return None


@st.cache_data(ttl=600, show_spinner=False)
def load_weather(city, api_key):
    return (
        get_current_weather(city, api_key),
        get_forecast_data(city, days=3, key=api_key),
    )


def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9


st.title("⛅ Interactive Weather Dashboard")
st.markdown(
    "Explore current conditions and a three-day forecast using live data from "
    "[WeatherAPI](https://www.weatherapi.com/). Enter a location and adjust the "
    "temperature unit to interact with the visualization."
)

with st.sidebar:
    st.header("Search settings")
    city = st.text_input("City or ZIP code", value="New York").strip()
    unit = st.radio("Temperature unit", ("°F", "°C"), horizontal=True)
    search = st.button("Update dashboard", type="primary", width="stretch")

if search or "weather_city" not in st.session_state:
    st.session_state.weather_city = city

selected_city = st.session_state.weather_city
api_key = get_api_key()

if not api_key:
    st.error(
        "Weather data is unavailable because WEATHER_API_KEY is not configured. "
        "Add it to a local .env file or Streamlit Community Cloud secrets."
    )
    st.stop()

if not selected_city:
    st.warning("Enter a city or ZIP code to view weather data.")
    st.stop()

with st.spinner("Loading weather data..."):
    current, forecast = load_weather(selected_city, api_key)

if not current or not forecast:
    st.error("Weather data could not be loaded. Check the location and try again.")
    st.stop()

st.header("Overview")
st.write(
    f"Showing live conditions for **{current['city']}, "
    f"{current['region'] or current['country']}**."
)

temperature = current["temperature"]
feels_like = current["feels_like"]
if unit == "°C":
    temperature = fahrenheit_to_celsius(temperature)
    feels_like = fahrenheit_to_celsius(feels_like)

primary_metrics = st.columns(2)
secondary_metrics = st.columns(2)
primary_metrics[0].metric("Temperature", f"{temperature:.1f}{unit}")
primary_metrics[1].metric("Feels like", f"{feels_like:.1f}{unit}")
secondary_metrics[0].metric("Humidity", f"{current['humidity']}%")
secondary_metrics[1].metric("Wind speed", f"{current['wind_speed']} mph")
st.info(f"Current condition: **{current['condition']}**")

st.header("Three-Day Forecast")
st.write(
    "The chart compares the forecast high, average, and low temperatures. "
    "Hover over a point to see its exact value."
)

forecast_df = pd.DataFrame(forecast)
forecast_df["date"] = pd.to_datetime(forecast_df["date"])
temperature_columns = ["max_temp_f", "avg_temp_f", "min_temp_f"]
if unit == "°C":
    forecast_df[temperature_columns] = forecast_df[temperature_columns].map(
        fahrenheit_to_celsius
    )

chart_df = forecast_df.rename(
    columns={
        "max_temp_f": "High",
        "avg_temp_f": "Average",
        "min_temp_f": "Low",
    }
).melt(
    id_vars="date",
    value_vars=["High", "Average", "Low"],
    var_name="Temperature range",
    value_name="Temperature",
)

figure = px.line(
    chart_df,
    x="date",
    y="Temperature",
    color="Temperature range",
    markers=True,
    title=f"Three-Day Temperature Forecast for {current['city']}",
    labels={"date": "Date", "Temperature": f"Temperature ({unit})"},
)
figure.update_layout(legend_title_text="Forecast")
figure.update_xaxes(dtick="D1", tickformat="%a<br>%b %d")
figure.update_traces(hovertemplate="%{y:.1f}<extra>%{fullData.name}</extra>")
st.plotly_chart(figure, use_container_width=True)

st.subheader("Data Display")
display_df = forecast_df.rename(
    columns={
        "date": "Date",
        "max_temp_f": f"High ({unit})",
        "avg_temp_f": f"Average ({unit})",
        "min_temp_f": f"Low ({unit})",
        "humidity": "Humidity (%)",
        "condition": "Condition",
    }
)
display_df["Date"] = display_df["Date"].dt.strftime("%a, %b %d")
display_df[[f"High ({unit})", f"Average ({unit})", f"Low ({unit})"]] = display_df[
    [f"High ({unit})", f"Average ({unit})", f"Low ({unit})"]
].round(1)
st.dataframe(
    display_df[
        [
            "Date",
            f"High ({unit})",
            f"Average ({unit})",
            f"Low ({unit})",
            "Humidity (%)",
            "Condition",
        ]
    ],
    hide_index=True,
    width="stretch",
)

st.header("Insights")
warmest = forecast_df.loc[forecast_df["max_temp_f"].idxmax()]
coolest = forecast_df.loc[forecast_df["min_temp_f"].idxmin()]
insight_columns = st.columns(2)
insight_columns[0].success(
    f"Warmest forecast: {warmest['date']:%A} at "
    f"{warmest['max_temp_f']:.1f}{unit}."
)
insight_columns[1].info(
    f"Coolest forecast: {coolest['date']:%A} at "
    f"{coolest['min_temp_f']:.1f}{unit}."
)
st.caption("Data source: WeatherAPI. Forecasts may change as new observations arrive.")
