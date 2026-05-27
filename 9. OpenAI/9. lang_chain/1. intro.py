# pip install langchain langchain-openai
import os
from dotenv import load_dotenv

from langchain_openai import OpenAI

load_dotenv()
openai_api_key = os.environ.get('OPEN_API_KEY')

lim = OpenAI(model='gpt-4o-mini')
print('lim:', lim)

prompt = '저녁으로 무엇을 먹을 지 추천해줘'
result = lim.invoke(prompt)
print('result:', result)