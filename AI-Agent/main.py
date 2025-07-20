from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

print("Dotenv loaded successfully")

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  


if api_key is None:
    raise Exception("OPENAI_API_KEY not found. Make sure it's in your .env file!")

llm = ChatOpenAI(model="gpt-4o-mini", api_key="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")


response = llm.invoke("What is the meaning of life?")
print(response)
