# pip install requests
# ollama pull qwen2.5:1.5

import requests

MODEL_NAME = 'qwen2.5:1.5b'

def ask_qwen(question):
    res = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': MODEL_NAME,
            'prompt': question,
            'stream': False
        })
    data = res.json()
    return data['response']

while True:
    user_input = input('Me: ')
    if user_input == 'exit':
        print('-' * 50, 'EXIT', '-' * 50)
        break
    print('Qwen: ', ask_qwen(user_input))