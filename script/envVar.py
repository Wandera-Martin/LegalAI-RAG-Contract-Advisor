import os
from dotenv import load_dotenv
load_dotenv()

openai = os.environ('OPENAI_API_KEY')
langchain = os.environ('LANGCHAIN_API_KEY')
langchain_tracing = os.environ('LANGCHAIN_TRACING_V2')

print(openai, langchain)
