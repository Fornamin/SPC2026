from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'abc1234' 
# Session 환경 변수 
# Session -> file / redis / memcached / mongod 등 지원
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['SESSION_FILE_DIR'] = './sessions'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

Session(app)

@app.route('/set-session')
def set_session():
    # 사용자에게는 세션ID만 주고 세션 데이터는 서버에 저장
    session['username'] = 'spc2026'
    session['dob'] = '2020/05/05'
    session['hobby'] = 'watching youtube, shopping, playing a game'

    return 'Session is set!'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f'Session is found\n{session['username']}, {session['dob']}, {session['hobby']}'
    return 'No Session'

if __name__ == '__main__':
    app.run(debug=True)