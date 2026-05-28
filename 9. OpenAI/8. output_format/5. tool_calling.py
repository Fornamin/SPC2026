import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_weather(city):
    weather = {'서울': '맑음, 22도', '부산': '흐림, 25도', 'LA': '비, 18도'}
    return weather.get(city, '해당 도시의 날씨 정보는 없습니다')

tools = [{
    'type': 'function',
    'function': {
        'name': 'get_weather',
        'description': '특정 도시의 현재 날씨를 조회',
        'parameters': {
            'type': 'object',
            'properties': {
                'city': {'type': 'string', 'description': '도시의 이름'}
            },
            'required': ['city']
        }
    }
}]
messages = [
    {'role': 'system', 'content': '질문에 답하세요.'},
    {'role': 'user', 'content': '서울의 현재 날씨는?'}
]

# 1차 호출
res = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages,
    tools=tools,
    tool_choice='auto'
)

message = res.choices[0].message
if message.tool_calls:
    tool_call = message.tool_calls[0]

    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    result = get_weather(arguments['city'])
    messages.append(message)

    messages.append({
        'role': 'tool',
        'tool_call_id': tool_call.id,
        'content': result
    })

    # 2차 호출
    final_res = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages
    )

    print(final_res.choices[0].message.content)