from langchain.tools import tool

@tool
def generate_day_plan(city: str, day_number: int) -> str:
    """
    Create a rough day itinerary for a given city and day.

    Args:
        city (str): The city of visit.
        day_number (int): The day number (e.g., 1 for Day 1).

    Returns:
        str: Itinerary plan for that day.
    """

    
    print("**********************************************************")
    print("Entered generate_day_plan")
    print("**********************************************************")

    return (
        f"Day {day_number} in {city}:\n"
        f"- Morning: Visit major landmarks\n"
        f"- Afternoon: Enjoy local food\n"
        f"- Evening: Attend a cultural event or nightlife spot"
    )


@tool
def generate_full_itinerary(city: str, days: int) -> str:
    """
    Generate a full itinerary for the entire trip.

    Args:
        city (str): City name.
        days (int): Number of days.

    Returns:
        str: Full trip plan.
    """


    print("**********************************************************")
    print("Entered generate_full_itinerary")
    print("**********************************************************")


    return "\n\n".join([generate_day_plan(city, i + 1) for i in range(days)])
