# from langchain_community.agent_toolkits.amadeus.toolkit import AmadeusToolkit
# from app.config import settings
# from amadeus import Client

# amadeus_client = Client(
#     client_id=settings.AMADEUS_CLIENT_ID,
#     client_secret=settings.AMADEUS_CLIENT_SECRET
# )

# AmadeusToolkit.model_rebuild(force=True)

# def get_hotel_tools(llm):

#     print("**********************************************************")
#     print("Entered get_hotel_tools")
#     print(llm)
#     print("**********************************************************")
#     AmadeusToolkit.model_rebuild(force=True)

#     amadeus_client = Client(
#         client_id=settings.AMADEUS_CLIENT_ID,
#         client_secret=settings.AMADEUS_CLIENT_SECRET
#     )

#     toolkit = AmadeusToolkit(
#         client=Client(
#             client_id=settings.AMADEUS_CLIENT_ID,
#             client_secret=settings.AMADEUS_CLIENT_SECRET
#         ),
#         llm=llm,
#         verbose=True,
#     )
#     tools = toolkit.get_tools()

#     print("**********************************************************")
#     print(tools)
#     print("**********************************************************")

#     return tools





    # [
    #     tool for tool in toolkit.get_tools()
    #     if "hotel" in tool.name.lower()  # or just return all tools if needed
    # ]

# Store hotel results temporarily for reuse
# _cached_hotels = []


# def search_hotels(city: str) -> list:
#     """
#     Searches for available hotels in the specified city.

#     Args:
#         city (str): The name of the city to search for hotels.

#     Returns:
#         list: A list of strings describing hotel names and prices.
#     """
#     global _cached_hotels

#     try:
#         query = f"Find hotels in {city}"
#         result = hotel_search_tool.invoke(query)

#         if not isinstance(result, list):
#             _cached_hotels = []
#             return [f"No hotels found: {result}"]

#         _cached_hotels = result
#         hotel_lines = []
#         for i, hotel in enumerate(result):
#             name = hotel.get("name", "Unknown Hotel")
#             price = hotel.get("price", "N/A")
#             hotel_lines.append(f"{i+1}. {name} - {price}")

#         return hotel_lines

#     except Exception as e:
#         return [f"⚠️ Error fetching hotels: {str(e)}"]

# def estimate_total_hotel_cost(city: str, days: int) -> float:
#     """
#     Estimates the total hotel cost for a given city and number of days
#     based on the average nightly rate of the cached hotel search.

#     Args:
#         city (str): The name of the city.
#         days (int): Number of nights to stay.

#     Returns:
#         float: Estimated total cost in USD.
#     """
#     if not _cached_hotels:
#         search_hotels(city)

#     prices = []
#     for hotel in _cached_hotels:
#         try:
#             price_str = hotel.get("price", "").replace("$", "").strip()
#             prices.append(float(price_str))
#         except (ValueError, AttributeError):
#             continue

#     if not prices:
#         return 0.0

#     avg_price = sum(prices) / len(prices)
#     return round(avg_price * days, 2)

# def budget_range(city: str, level: str = "mid") -> str:
#     """
#     Filters hotels based on a budget level: 'low', 'mid', or 'high'.

#     Args:
#         city (str): The name of the city.
#         level (str): Budget level - 'low', 'mid', or 'high'.

#     Returns:
#         str: A formatted string listing hotels in the specified price range.
#     """
#     if not _cached_hotels:
#         search_hotels(city)

#     filtered = []
#     for hotel in _cached_hotels:
#         try:
#             price = float(hotel.get("price", "").replace("$", "").strip())
#             if level == "low" and price < 100:
#                 filtered.append(hotel)
#             elif level == "mid" and 100 <= price < 200:
#                 filtered.append(hotel)
#             elif level == "high" and price >= 200:
#                 filtered.append(hotel)
#         except (ValueError, AttributeError):
#             continue

#     if not filtered:
#         return f"No {level}-range hotels found in {city}."

#     return "\n".join([f"{h['name']} - {h['price']}" for h in filtered])