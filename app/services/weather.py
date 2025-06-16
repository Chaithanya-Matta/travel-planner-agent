from langchain_community.utilities import OpenWeatherMapAPIWrapper
from app.config import settings
from datetime import datetime
import requests

OPENWEATHERMAP_API_KEY = settings.OPENWEATHERMAP_API_KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
weather_api = OpenWeatherMapAPIWrapper(openweathermap_api_key=OPENWEATHERMAP_API_KEY)

def get_current_weather(city: str) -> str:
    """
    Get current weather info for a given city using OpenWeatherMap.

    Args:
        city (str): Name of the city (e.g., "Paris", "New York")

    Returns:
        str: Human-readable summary of current weather conditions.
    """

    print("**********************************************************")
    print("Entered get_current_weather")
    print("**********************************************************")

    try:
        return weather_api.run(city)
    except Exception as e:
        return f"⚠️ Unable to fetch weather data: {str(e)}"

def get_weather_forecast(city: str, days: int = 3) -> str:
    """
    Fetch a short-term (3-5 days) weather forecast for a city.

    Args:
        city (str): City name (e.g., "London").
        days (int): Number of days to forecast (max 5).

    Returns:
        str: A human-readable weather summary.
    """

    print("**********************************************************")
    print("Entered get_weather_forecast")
    print("**********************************************************")

    if not OPENWEATHERMAP_API_KEY:
        return "⚠️ OpenWeather API key not set."

    try:
        params = {
            "q": city,
            "appid": OPENWEATHERMAP_API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        forecast_data = data.get("list", [])
        if not forecast_data:
            return f"⚠️ No forecast data found for {city}."

        # Forecasts are in 3-hour steps; group by day
        output = f"Weather forecast for {city} (next {days} days):\n"
        current_day = ""
        count = 0

        for entry in forecast_data:
            timestamp = entry["dt"]
            date_str = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
            time_str = datetime.utcfromtimestamp(timestamp).strftime('%H:%M')
            temp = entry["main"]["temp"]
            desc = entry["weather"][0]["description"]

            if date_str != current_day:
                count += 1
                current_day = date_str
                output += f"\n📅 {date_str}:\n"

            output += f"  - {time_str} → {temp:.1f}°C, {desc}\n"

            if count >= days:
                break
        # print("**********************************************************")
        # print(output)
        # print("**********************************************************")
        return output
    
    except requests.RequestException as e:
        return f"⚠️ API request failed: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"