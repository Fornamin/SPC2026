import requests
import os
from dotenv import load_dotenv

load_dotenv() # 경로 지정 가능
openai_api_key = os.getenv('OPENAI_API_KEY')

user_input = '대한민국의 수도는 어디입니까'
res = requests.post(
    'https://api.openai.com/v1/responses',
    headers={
        'Content-Type':'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    },
    json={
        'model': 'gpt-4o-mini',
        'input': user_input
    }
)
data = res.json()
print(data['output'][0]['content'][0]['text'])