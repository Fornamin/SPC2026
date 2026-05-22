from flask import Flask, send_from_directory, request, jsonify
from flask import session

import openai

from dotenv import load_dotenv
import os

import sqlite3

load_dotenv()

conn = sqlite3.connect('openai-chat.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = 'your_secret_key'

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def init_db():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS session (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL)
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')
    conn.commit()

def create_session():
    cur.execute('''
        INSERT INTO session(user_id) VALUES(?)
        ''', (session.get('user_id')))
    conn.commit()
    
def refresh_chat():
    cur.execute(f'''
        DELETE FROM chat WHERE session_id = "{session.get('current_session_id')}"
        ''')
    conn.commit()

def read_latest_chat(count):
    cur.execute(f'''
    SELECT * FROM (
        SELECT * FROM chat 
        WHERE session_id = "{session.get('current_session_id')}"
        ORDER BY timestamp DESC 
        LIMIT {count}
    )
    ORDER BY id ASC
    ''')

    rows = cur.fetchall()
    result = [dict(row) for row in rows]

    return result

def read_all_chat():
    cur.execute(f'''
    SELECT * FROM chat WHERE session_id = "{session.get('current_session_id')}"
    ORDER BY id
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

def get_all_session():
    cur.execute(f'''
        SELECT * FROM session WHERE user_id="{session.get('user_id')}" ORDER BY id DESC
        ''')
    session_id_list = cur.fetchall()
    if (session_id_list == None):
        return None, None

    session['current_session_id'] = len(session_id_list) + 1

    latest_chat_list = []
    for item in session_id_list:
        cur.execute(f'''
            SELECT * FROM chat WHERE session_id="{item['id']}" ORDER BY id DESC LIMIT 1
            ''')
        latest_chat_list.append(cur.fetchone())

    return session_id_list, latest_chat_list
    
@app.route('/')
def index():
    init_db()

    session['user_id'] = 'guest'

    # 지난 대화 목록
    session_id_list, latest_chat_list = get_all_session()
    if session_id_list == None:
        create_session()

    return send_from_directory('static', 'index.html')

@app.route('/api/session')
def get_session():
    pass

@app.route('/api/chat/', methods=['POST'])
def chat():
    session_id = session.get('current_session_id')

    # user에게서 질문을 받아옴
    data = request.get_json()
    chat_msg = data.get('chatMsg', '')

    cur.execute('INSERT INTO chat (session_id, role, content) VALUES(?, ?, ?)', 
                (session_id, 'user', chat_msg))
    
    # chat-gpt에게 요청
    res_msg = ask_chatgpt()
    cur.execute('INSERT INTO chat (session_id, role, content) VALUES(?, ?, ?)', 
                (session_id, 'system', res_msg))
    conn.commit()

    # ChatGPT에게 요청 후 응답 가져오기
    return jsonify({'reply': res_msg})

@app.route('/api/chat-all/')
def chat_all():
    return read_all_chat()

@app.route('/api/refresh', methods=['GET'])
def refresh():
    refresh_chat()
    return jsonify({'response': 'success'})

if __name__ == '__main__':
    app.run(debug=True)