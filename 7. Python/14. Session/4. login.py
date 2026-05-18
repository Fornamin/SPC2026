from flask import Flask, render_template, request
from flask import session
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'my-random-key'

users = [
    {"name": "Kim Minsoo", "id": "minsoo01", "pw": "a1234"},
    {"name": "Lee Jihyun", "id": "jihyun22", "pw": "b5678"},
    {"name": "Park Junho", "id": "junho77", "pw": "c9012"},
    {"name": "Choi Yuna", "id": "yuna99", "pw": "d3456"},
    {"name": "Jung Hyerin", "id": "hyerin15", "pw": "e7890"},
]

def form_login(id, pw): 
    for u in users: 
        if u['id'] == id and u['pw'] == pw: 
            return u

@app.route('/dashboard')
def welcome():
    user = session.get('user')
    return render_template('dashboard.html', name=user['name'])

@app.route('/', methods=['GET'])
def home():
    user = None

    if session:
        user = form_login(session['user']['id'], session['user']['pw'])
        return redirect(url_for('welcome'))

    return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    id = request.form['userId']
    pw = request.form['userPw']
    user = form_login(id, pw)

    if user:
        session['user'] = user
        error = None
        return redirect(url_for('welcome'))
    else:
        error = 'Invalid Id or Password'
        
    return render_template('index.html', error = error)
    
@app.route('/logout')
def logout():
    session.pop('user', None)
      
    return redirect(url_for('home'))

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    user = session.get('user')
    msg = None

    if not user:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        new_password = request.form['userPw']
        msg = 'Password is changed'
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_password
                session['user'] = u
                break
    
    return render_template('profile.html', user = session.get('user'), msg = msg)

if __name__ == '__main__':
    app.run(debug=True)