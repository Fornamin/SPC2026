from flask import Flask, render_template, request
from flask import redirect, url_for
from flask import session, flash

import sqlite3

from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'MY_SECRET_KEY'
app.permanent_session_lifetime = timedelta(minutes=5)

DATABASE = 'miniapp-users.sqlite3'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # result를 dict로 관리하겠다
    cur = conn.cursor()

    return conn

def init_db():
    with app.app_context(): # Flask app 초기화 완료 후 
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT
            )''')

        cur.execute('SELECT COUNT(*) AS count FROM users')
        count = cur.fetchone()['count']

        if count == 0:
            cur.execute('INSERT INTO users (user_id, password, email) VALUES (?, ?, ?)',
                        ('user1', '1234', 'user1@example.com'))
            cur.execute('INSERT INTO users (user_id, password) VALUES (?, ?)',
                        ('user2', '1234'))
            
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print('-' * 60)
        for row in rows:
            print(row['id'], row['user_id'], row['password'])
        print('-' * 60)

        conn.commit()
        conn.close()
        

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        userId = request.form['userId']
        userPw = request.form['userPw']
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE user_Id = ? and password = ?',
                    (userId, userPw))
        userdata = cur.fetchone()
        conn.close

        if userdata:
            session['user'] = userId
            flash('Login successed')
            return redirect(url_for('home'))
        else:
            flash('Login failed')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('Logout successed')
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    user = session['user']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'DELETE FROM users WHERE user_id = "{user}"')
    conn.commit()
    conn.close()
    flash('GoodBye')
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userId = request.form.get('userId')
        userPw = request.form.get('userPw')
        userEmail = request.form.get('userEmail')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE user_id = ?', (userId, ))
        existingUser = cur.fetchone()
        if existingUser:
            flash('Unavailable Id')
            conn.close()
            return redirect(url_for('signup'))
        cur.execute('INSERT INTO users (user_id, password, email) VALUES (?, ?, ?)',
                    (userId, userPw, userEmail))
        conn.commit()
        conn.close()
        session['user'] = userId
        flash('Sign up successed')
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # 1. DB에서 나의 정보를 조회
    # 2. 정보를 넘김
    # 3. 수정 기능
    user = session.get('user')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user, ))
    userData = cur.fetchone()
    if userData:
        for item in userData:
            print(item)

    if request.method == 'POST':
        userId = request.form.get('userId')
        userPw = request.form.get('userPw')
        userEmail = request.form.get('userEmail')

        query = f'UPDATE users SET user_id = ?, password = ?, email = ? WHERE user_id = "{user}"'
        cur.execute(query, (userId, userPw, userEmail))
        conn.commit()
        conn.close()
        session['user'] = userId

        return redirect(url_for('profile'))

    return render_template('profile.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)