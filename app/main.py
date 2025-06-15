from fastapi import FastAPI
from app.routers import travel

app = FastAPI(title="AI Travel Agent & Expense Planner")
app.include_router(travel.router)

@app.get("/")
def home():
    return {"message": "Travel Agent API is up!"}