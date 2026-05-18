from flask import Flask, render_template, request

app = Flask(__name__)

# localDB
users = [
    {'name': '홍길동', 'id': 'hong', 'pw': '1234'},
    {'name': '김철수', 'id': 'kim', 'pw': '1111'},
    {'name': '이영희', 'id': 'lee', 'pw': '2222'},
    {'name': '박민수', 'id': 'park', 'pw': '3333'},
    {'name': '최지훈', 'id': 'choi', 'pw': '4444'},
    {'name': '정수빈', 'id': 'jung', 'pw': '5555'},
    {'name': '한예진', 'id': 'han', 'pw': '6666'},
    {'name': '오세훈', 'id': 'oh', 'pw': '7777'},
    {'name': '윤도현', 'id': 'yoon', 'pw': '8888'},
    {'name': '장민지', 'id': 'jang', 'pw': '9999'}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    user = None
    error = None

    if request.method == 'POST':
        id = request.form['userId']
        pw = request.form['userPw']

        for u in users:
            if u['id'] == id and u['pw'] == pw: user = u
        
        if user == None: error = 'Invalid Id or Password'
        return render_template('index.html', user=user, error=error)

    return render_template('index.html', user=user, error=error)

if __name__ == '__main__':
    app.run(debug=True)