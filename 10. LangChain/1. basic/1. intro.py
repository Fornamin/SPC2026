# pip install langchain langchain-openai
import os
from dotenv import load_dotenv

from langchain_openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(model='gpt-4o-mini', temperature=1.0)
print('llm:', llm)

prompt = 'recommend what to eat'
result = llm.invoke(prompt)
print('result:', result)