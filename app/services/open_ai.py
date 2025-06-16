from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage
# from langchain_core.embeddings import Embeddings
from app.config import settings
from typing import List
from langsmith import Client
import os

class OpenAIService:
    def __init__(self):
        # os.environ["LANGCHAIN_TRACING_V2"] = "true"
        # os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY
        # os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT
        # self.client = Client(
        #     api_key=settings.LANGCHAIN_API_KEY
        # )
        self.chat_model: BaseChatModel = ChatOpenAI(
            model=settings.OPENAI_CHAT_MODEL,
            temperature=1,
            api_key=settings.OPENAI_API_KEY
        )

        # self.embedding_model: Embeddings = OpenAIEmbeddings(
        #     model=settings.OPENAI_EMBEDDING_MODEL,
        #     api_key=settings.OPENAI_API_KEY
        # )

    def get_chat_response(self, messages: List[BaseMessage]) -> str:
        """
        Accepts a list of LangChain message objects (e.g., SystemMessage, HumanMessage)
        """
        return self.chat_model.invoke(messages).content
    
    # def get_chat_response(self, messages: List[dict]) -> str:
    #     """
    #     Accepts list of messages in OpenAI format:
    #     [{"role": "user", "content": "Hello"}]
    #     """
    #     return self.chat_model.invoke(messages).content
    
    # def get_embeddings(self, texts: List[str]) -> List[List[float]]:
    #     """
    #     Accepts a list of strings and returns list of embeddings.
    #     """
    #     return self.embedding_model.embed_documents(texts)
    
    # def get_embedding(self, text: str) -> List[float]:
    #     """
    #     Accepts a list of strings and returns list of embeddings.
    #     """
    #     return self.embedding_model.embed_query(text)