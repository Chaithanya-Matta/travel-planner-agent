from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain.tools import tool

search = DuckDuckGoSearchRun()

@tool
def search_attractions(city: str) -> str:
    """
    Search for top tourist attractions in the given city. This is a open web search using DuckDuckGo.

    Args:
        city (str): City to search in.

    Returns:
        str: A list or description of popular attractions.
    """

    print("**********************************************************")
    print("Entered search_attractions")
    print("**********************************************************")

    query = f"Top tourist attractions in {city}"
    return search.run(query)


@tool
def search_activities(city: str) -> str:
    """
    Search for popular activities in the given city. This is a open web search using DuckDuckGo.

    Args:
        city (str): City to search in.

    Returns:
        str: A list of interesting activities.
    """
    
    print("**********************************************************")
    print("Entered search_activities")
    print("**********************************************************")

    query = f"Popular activities to do in {city}"
    return search.run(query)