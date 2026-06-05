# 외부에 있는 ollama 서버에 req 요청

import requests

OLLAMA_HOST = 'http://127.0.0.1:11434'
OLLAMA_ENDPOINT = f'{OLLAMA_HOST}/api/generate'

payload = {
    'model': 'exaone3.5:2.4b',
    'prompt': '파이썬으로 "Hello World"를 출력하는 코드를 구현해줘',
    'stream': False
}

res = requests.post(OLLAMA_ENDPOINT, json=payload)
data = res.json()

print('[MODEL RESPONSE]', data['response'])