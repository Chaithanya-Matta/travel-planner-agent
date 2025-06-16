from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition 
from langgraph.graph import MessagesState, StateGraph
from app.services.open_ai import OpenAIService
from app.tools.tool_registry import get_all_tools
from langsmith import traceable

# Setup LLM bound with tools
# llm = OpenAIService().chat_model.bind_tools(TOOLS)

open_ai_service = OpenAIService()
llm = open_ai_service.chat_model
TOOLS = get_all_tools(llm = llm)
llm_with_tools = llm.bind_tools(TOOLS)

# System prompt
SYSTEM_PROMPT = SystemMessage(content="""
                                FYI - This is still in development. The tools are not ready yet. I will be testing this functionality. Please play along.
                                You are a helpful AI travel assistant.
                                The user will provide the destination and the number of days for their trip.
                                Please assist with information about the weather, attractions, hotels, itinerary, and total cost.
                                By default, use the local currency of the destination unless the user specifies otherwise.
                                """)

# LLM function node
def react_llm(state: MessagesState):
    history = state["messages"]
    inputs = [SYSTEM_PROMPT] + history
    response = llm_with_tools.invoke(inputs)
    return {"messages": [response]}

# Build LangGraph
builder = StateGraph(MessagesState)
builder.add_node("travel_planner_agent", react_llm)
builder.add_node("tools", ToolNode(TOOLS))
builder.set_entry_point("travel_planner_agent")
builder.add_conditional_edges("travel_planner_agent", tools_condition)
builder.add_edge("tools", "travel_planner_agent")
builder.set_finish_point("travel_planner_agent")

travel_graph = builder.compile()

# Entry function
@traceable(name="run_travel_agent")
async def run_travel_agent(message: str):
    history = [HumanMessage(content=message)]
    response = travel_graph.invoke({"messages": history})
    return response["messages"][-1].content