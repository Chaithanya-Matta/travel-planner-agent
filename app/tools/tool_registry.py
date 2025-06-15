from langchain.tools import tool

# Dummy implementations for now — will connect to real APIs later

@tool
def get_weather(city: str) -> str:
    """Get current weather in the given city."""
    return f"The weather in {city} is sunny and 25°C."

@tool
def search_hotels(city: str, days: int) -> float:
    """Estimate total hotel cost in a city for N days."""
    return days * 120.0  # Assume $120/night

@tool
def get_attractions(city: str) -> str:
    """Get top attractions for a city."""
    return f"Top attractions in {city} include museums, parks, and monuments."

@tool
def convert_currency(amount: float, to_currency: str) -> float:
    """Convert amount to a target currency."""
    exchange_rate = 0.92 if to_currency.lower() == "eur" else 1.0
    return amount * exchange_rate

# List of all available tools
TOOLS = [get_weather, search_hotels, get_attractions, convert_currency]
