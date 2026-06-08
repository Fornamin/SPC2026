from flask import Flask, send_from_directory
from flask import request, jsonify

import os
from dotenv import load_dotenv

import json
import requests

import openai

app = Flask(__name__, static_folder='public', static_url_path='')

openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/api/codecheck', methods=['POST'])
def code_check():
    prompt = '당신은 경력 10년차의 개발자입니다.\
            다음 코드를 보고 취약점을 분석하시오.\
            각 취약점에 대해 해당 코드의 라인 번호, 코드 스니펫, 취약점 설명과 개선 방안을 간단하게 설명하시오.\
            그리고 다음 옵션을 참고하시오. (빈 칸일 시 옵션 없음)'
    
    option = request.json.get('option')
    for key, value in option.items():
        if value == True:
            prompt += f'{key}가 발생할 수 있는가?'
        
    def get_raw_code():
        code_link = request.json.get('code_link', '').split('/')
        raw_code_link = (
        f"{code_link[0]}//raw.githubusercontent.com/"
        f"{code_link[3]}/{code_link[4]}/refs/heads/"
        f"{'/'.join(code_link[6:])}")
        
        return requests.get(raw_code_link).text  
      
    def ask_chatgpt():
        res = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': prompt},
                      {'role': 'user', 'content': get_raw_code()}]
        )
        return res.choices[0].message.content
    return jsonify({'result': ask_chatgpt(), 'code': get_raw_code()})

if __name__ == '__main__':
    app.run(debug=True)