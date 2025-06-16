from langchain.tools import tool
from app.services.weather import (
    get_current_weather as fetch_current_weather,
    get_weather_forecast as fetch_weather_forecast
)
from app.services.itinerary import generate_full_itinerary, generate_day_plan
from app.services.search import search_attractions, search_activities
# from app.services.hotels import get_hotel_tools
# search_hotels, estimate_total_hotel_cost, budget_range, get_hotel_tools

@tool
def get_current_weather(city: str) -> str:
    """
    Get current weather for a given city using OpenWeatherMap.
    Returns a human-readable summary.
    """
    return fetch_current_weather(city)

@tool
def get_weather_forecast(city: str, days: int = 3) -> str:
    """
    Get a multi-day weather forecast for a given city (up to 5 days).
    FYI from developer : 
    OpenWeatherMapAPIWrapper currently does not support real forecasts — it’s limited to current weather.
    Forecasts are in 3-hour steps; our wrapper method groups by day
    """
    return fetch_weather_forecast(city, days)

@tool
def convert_currency(amount: float, to_currency: str) -> float:
    """Convert amount to a target currency."""
    exchange_rate = 0.92 if to_currency.lower() == "eur" else 1.0
    return amount * exchange_rate

# List of all available tools
TOOLS = [get_current_weather, 
         get_weather_forecast, 
         generate_full_itinerary, 
         generate_day_plan, 
         search_attractions, 
         search_activities, 
         convert_currency]

def get_all_tools(llm=None):
    print("**********************************************************")
    print("Entered get_all_tools")
    # print(llm)
    print("**********************************************************")
    tools = TOOLS
    # tools += get_hotel_tools(llm)
    return tools