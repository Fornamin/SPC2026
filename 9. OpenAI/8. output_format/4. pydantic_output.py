import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from pydantic import BaseModel

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class CityInfo(BaseModel):
    name: str
    population: int
    area_km2: float

res = client.chat.completions.parse(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': '질문에 JSON으로만 답변하세요.'},
        {'role': 'user', 'content': '서울의 인구와 면적은?'}],
    response_format=CityInfo) 

data = res.choices[0].message.parsed
print(f'도시: {data.name}\n인구: {data.population:,}명 / 면적: {data.area_km2}km2')
