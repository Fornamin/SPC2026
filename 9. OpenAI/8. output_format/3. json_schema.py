import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Json Schema를 정의
city_schema = { # 내가 원하는 변수 및 데이터 타입
    'type': 'object',
    'properties': {
        'name':         {'type': 'string'},
        'population':   {'type': 'integer'},
        'area_km2':     {'type': 'number'},
    },
    'required': ['name', 'population', 'area_km2'],
    'additionalProperties': False,
}

res = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': '질문에 JSON으로만 답변하세요.'},
        {'role': 'user', 'content': '서울의 인구와 면적은?'}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "city_info",
            "strict": True,
            "schema": city_schema
        }
    }) # 출력 결과가 직접 정의한 스키마로 오도록 요청

answer = res.choices[0].message.content
data = json.loads(answer)

print(f'도시: {data['name']}\n인구: {data['population']:,}명 / 면적: {data['area_km2']}km2')