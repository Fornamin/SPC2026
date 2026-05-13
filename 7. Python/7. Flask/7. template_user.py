from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_names = [
        '김민정',
        '이서연',
        '박지훈',
        '최유진',
        '정현우',
        '한지민',
        '윤서준',
        '강다은',
        '조민재',
        '임수빈',
        '오지훈',
        '신예린',
        '서도윤',
        '권나연',
        '황민석',
        '송하은',
        '유태윤',
        '백지원',
        '문준혁',
        '안채린'
    ]
    html = render_template('users.html', names = user_names)
    return html

if __name__ == '__main__':
    app.run(debug=True)