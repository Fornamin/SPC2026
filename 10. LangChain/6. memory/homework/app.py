from flask import (
    Flask, render_template, 
    jsonify, redirect, url_for,
    session
)

app = Flask(__name__)

@app.route('/')
def main():
    # 세션 없으면 로그인으로
    return render_template('index.html')

@app.route('/login')
def login():
    # 로그인/세션 저장
    return render_template('login.html')

@app.route('/logout')
def logout():
    # 세션 삭제
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)