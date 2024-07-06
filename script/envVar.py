from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2")
cohere_api_key = os.getenv("COHERE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

print(f"OpenAI API Key: {openai_api_key}")
print(f"LangChain API Key: {langchain_api_key}")
print(f"LangChain Tracing V2: {langchain_tracing_v2}")
print(f"Cohere API Key: {cohere_api_key}")
print(f"Tavily API Key: {tavily_api_key}")
