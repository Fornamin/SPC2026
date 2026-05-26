import os
from dotenv import load_dotenv

import json

from flask import Flask, send_from_directory
from flask import request, Response

from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/stream', methods=['POST'])
def stream():
    #예외 처리 생략
    user_msg = request.json.get('msg', '')

    def generate_response():
        res = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': '당신은 친절한 AI 도우미'},
                {'role': 'system', 'content': user_msg}
            ],
            stream=True
        )
        for chunk in res:
            content = chunk.choices[0].delta.content
            if content:
                yield f'data: {json.dumps({'content': content}, ensure_ascii=False)}\n\n'
        yield 'data: [DONE]\n\n'
    return Response(generate_response(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)