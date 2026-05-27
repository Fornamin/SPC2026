import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

res = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{'role': 'system', 'content': '질문에 JSON으로만 답변하세요.'},
              {'role': 'user', 'content': '서울의 인구와 면적은?'}])

answer = res.choices[0].message.content
print(answer)