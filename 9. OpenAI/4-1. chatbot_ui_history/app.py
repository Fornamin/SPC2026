from flask import Flask, send_from_directory, request, jsonify

import openai

from dotenv import load_dotenv
import os

import sqlite3

load_dotenv()

conn = sqlite3.connect('openai.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

app = Flask(__name__, static_folder='static', static_url_path='')

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def init_db():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')
    conn.commit()

def refresh_chat():
    cur.execute('''
        DELETE FROM chat
        ''')
    conn.commit()

def read_latest_chat(count):
    cur.execute(f'''
    SELECT * FROM (
        SELECT * FROM chat 
        ORDER BY timestamp DESC 
        LIMIT {count}
    )
    ORDER BY id ASC
    ''')

    rows = cur.fetchall()
    # rows = rows[::-1] <- 이렇게 하면 서브 쿼리 안 써도 됨
    result = [dict(row) for row in rows]

    return result

def read_all_chat():
    cur.execute(f'''
    SELECT * FROM chat ORDER BY id
    ''')

    rows = cur.fetchall()
    result = [dict(row) for row in rows]

    return result

def ask_chatgpt():
    result = read_latest_chat(10);
    history = []
    for item in result:
        history.append({'role': item['role'], 'content': item['content']})

    res = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role': 'system', 'content': '넌 친절한 챗봇'}] + history)
    return res.choices[0].message.content

@app.route('/')
def index():
    init_db()

    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    # user에게서 질문을 받아옴
    data = request.get_json()
    chat_msg = data.get('chatMsg', '')
    cur.execute('INSERT INTO chat (role, content) VALUES(?, ?)', 
                ('user', chat_msg))
    
    # chat-gpt에게 요청
    res_msg = ask_chatgpt()
    # history.append({'role': 'system', 'content': res_msg})
    cur.execute('INSERT INTO chat (role, content) VALUES(?, ?)', 
                ('system', res_msg))
    conn.commit()

    # ChatGPT에게 요청 후 응답 가져오기
    return jsonify({'reply': res_msg})

@app.route('/api/chat-all')
def chat_all():
    return read_all_chat()

@app.route('/api/refresh', methods=['GET'])
def refresh():
    refresh_chat()
    return jsonify({'response': 'success'})

# 추후 사용자 별로 history 테이블이 관리 되어야 함

if __name__ == '__main__':
    app.run(debug=True)