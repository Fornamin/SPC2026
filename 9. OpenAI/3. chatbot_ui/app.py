from flask import Flask, send_from_directory
from flask import request, jsonify

import openai

from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__, static_folder='static', static_url_path='')

def ask_chatgpt(msg):
    res = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': '넌 친절한 챗봇'},
            {'role': 'user', 'content': msg}
        ])
    return res.choices[0].message.content

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    chat_msg = data.get('chatMsg', '')

    # ChatGPT에게 요청 후 응답 가져오기
    return jsonify({'reply': ask_chatgpt(chat_msg)})

if __name__ == '__main__':
    app.run(debug=True)