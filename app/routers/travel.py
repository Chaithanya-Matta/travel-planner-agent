from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.agents.travel_agent import run_travel_agent

router = APIRouter()

class TravelRequest(BaseModel):
    city: str
    days: int
    currency: str = "USD"

# @router.post("/plan-trip")
# async def plan_trip(input: TravelRequest):
#     # 👇 Create a natural language query for the agent
#     prompt = (
#         f"I want to plan a {input.days}-day trip to {input.city}. "
#         f"My preferred currency is {input.currency}. "
#         "Please help me with weather, attractions, hotels, itinerary, and total cost."
#     )

#     # 👇 Call the ReAct-style agent with the natural language prompt
#     result = await run_travel_agent(prompt)
#     return {"response": result}

@router.post("/chat")
async def chat_agent(message: str = Body(..., embed=True)):
    """
    Accepts a plain text chat message from the user and sends it to the ReAct agent.
    """
    response = await run_travel_agent(message)
    return {"response": response}