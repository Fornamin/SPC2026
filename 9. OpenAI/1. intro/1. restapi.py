import requests
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
user_input = '잘 먹었습니당'

res = requests.post(
    # /v1/chat/completions: 문장을 완성
    # /v1/responses: 응답 -> 서버 안에 메모리를 사용
    'https://api.openai.com/v1/chat/completions',
    json={
        'model': 'gpt-3.5-turbo', #gpt-4, gpt-4o, gpt-4o-mini, gpt-5 등 다양한 모델
        'messages': [
            {'role': 'system',
             'content': '너는 한국의 배달 어플 사장이고 고객 리뷰에 대한 답글을 작성하면 돼'},
            {'role': 'user',
             'content': user_input}
        ]
    },
    headers={
        'Content-Type':'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }
)

data = res.json()
print(data['choices'][0]['message']['content'])