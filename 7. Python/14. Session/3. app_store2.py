from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'abc1234' 
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['SESSION_FILE_DIR'] = './.sessions'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

Session(app)

@app.route('/')
def main():
    if 'username' in session:
        return f'Session is found\n{session['username']}, {session['dob']}, {session['hobby']}'
    
    session['username'] = 'spc2026'
    session['dob'] = '2020/05/05'
    session['hobby'] = 'watching youtube, shopping, playing a game'

    return 'Session is set!'

if __name__ == '__main__':
    app.run(debug=True)