from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT")
    LANGCHAIN_TRACING_V2: str = os.getenv("LANGCHAIN_TRACING_V2")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    OPENAI_CHAT_MODEL: str = os.getenv("OPENAI_CHAT_MODEL")
    OPENAI_EMBEDDING_MODEL: str = os.getenv("OPENAI_EMBEDDING_MODEL")
    OPENWEATHERMAP_API_KEY: str = os.getenv("OPENWEATHERMAP_API_KEY")
    AMADEUS_CLIENT_ID: str = os.getenv("AMADEUS_CLIENT_ID")
    AMADEUS_CLIENT_SECRET: str = os.getenv("AMADEUS_CLIENT_SECRET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()