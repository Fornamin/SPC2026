from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key' # 세션 암호화 키 -> .env에 저장하자

# curl 127.0.0.1:5000/set-session -c session.txt
# curl 127.0.0.1:5000/get-session -b session.txt

@app.route('/set-session')
def set_session():
    session['username'] = 'spc2026'
    return 'Session is set!'

@app.route('/get-session')
def get_session():
    # 정보는 서버에 저장되지만 사용자를 식별하기 위해 쿠키 사용 => 세션 ID
    # 위변조는 가능하지만 서버에서 값을 찾을 수 없어 소용X
    # 세션 저장소를 설정하지 않음 => 현재는 쿠키 저장소에 저장됨
    if 'username' in session:
        return f'Session is found / {session['username']}'
    return 'No Session'

if __name__ == '__main__':
    app.run(debug=True)