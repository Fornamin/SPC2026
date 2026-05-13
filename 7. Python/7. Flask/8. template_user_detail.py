from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'name': '김민준', 'age': 28, 'phone': '010-1234-5678'},
        {'name': '이서연', 'age': 31, 'phone': '010-2345-6789'},
        {'name': '박지훈', 'age': 25, 'phone': '010-3456-7890'},
        {'name': '최유진', 'age': 34, 'phone': '010-4567-8901'},
        {'name': '정현우', 'age': 29, 'phone': '010-5678-9012'},
        {'name': '한지민', 'age': 27, 'phone': '010-6789-0123'},
        {'name': '윤서준', 'age': 40, 'phone': '010-7890-1234'},
        {'name': '강다은', 'age': 22, 'phone': '010-8901-2345'},
        {'name': '조민재', 'age': 36, 'phone': '010-9012-3456'},
        {'name': '임수빈', 'age': 30, 'phone': '010-0123-4567'},
        {'name': '오지훈', 'age': 28, 'phone': '010-1122-3344'},
        {'name': '신예린', 'age': 33, 'phone': '010-2233-4455'},
        {'name': '서도윤', 'age': 26, 'phone': '010-3344-5566'},
        {'name': '권나연', 'age': 41, 'phone': '010-4455-6677'},
        {'name': '황민석', 'age': 24, 'phone': '010-5566-7788'},
        {'name': '송하은', 'age': 37, 'phone': '010-6677-8899'},
        {'name': '유태윤', 'age': 32, 'phone': '010-7788-9900'},
        {'name': '백지원', 'age': 45, 'phone': '010-8899-0011'},
        {'name': '문준혁', 'age': 23, 'phone': '010-9900-1122'},
        {'name': '안채린', 'age': 38, 'phone': '010-1010-2020'},
        {'name': '김하린', 'age': 29, 'phone': '010-2020-3030'},
        {'name': '이준서', 'age': 27, 'phone': '010-3030-4040'},
        {'name': '박소윤', 'age': 35, 'phone': '010-4040-5050'},
        {'name': '최도현', 'age': 42, 'phone': '010-5050-6060'},
        {'name': '정예은', 'age': 21, 'phone': '010-6060-7070'},
        {'name': '한성민', 'age': 39, 'phone': '010-7070-8080'},
        {'name': '윤아린', 'age': 28, 'phone': '010-8080-9090'},
        {'name': '강현준', 'age': 34, 'phone': '010-9090-1010'},
        {'name': '조서윤', 'age': 26, 'phone': '010-1111-2222'},
        {'name': '임지호', 'age': 31, 'phone': '010-2222-3333'},
        {'name': '오하윤', 'age': 25, 'phone': '010-3333-4444'}
    ]
    html = render_template('users_detail.html', users = users)
    return html

if __name__ == '__main__':
    app.run(debug=True)