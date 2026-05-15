# CSR
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "김민준", "email": "minjun1@example.com"},
    2: {"id": 2, "name": "이서연", "email": "seoyeon2@example.com"},
    3: {"id": 3, "name": "박지훈", "email": "jihoon3@example.com"},
    4: {"id": 4, "name": "최지우", "email": "jiwoo4@example.com"},
    5: {"id": 5, "name": "정예준", "email": "yejun5@example.com"},
    6: {"id": 6, "name": "한수아", "email": "sua6@example.com"},
    7: {"id": 7, "name": "윤도현", "email": "dohyun7@example.com"},
    8: {"id": 8, "name": "강하린", "email": "harin8@example.com"},
    9: {"id": 9, "name": "오준서", "email": "junseo9@example.com"},
    10: {"id": 10, "name": "서유진", "email": "yujin10@example.com"},
}
products = {

    101: {"id": 101, "name": "노트북", "price": 1200000},
    102: {"id": 102, "name": "마우스", "price": 35000},
    103: {"id": 103, "name": "키보드", "price": 89000},
    104: {"id": 104, "name": "모니터", "price": 270000},
    105: {"id": 105, "name": "이어폰", "price": 129000},
    106: {"id": 106, "name": "스마트폰", "price": 980000},
    107: {"id": 107, "name": "태블릿", "price": 650000},
    108: {"id": 108, "name": "웹캠", "price": 55000},
    109: {"id": 109, "name": "외장하드", "price": 145000},
    110: {"id": 110, "name": "프린터", "price": 210000},
}


@app.route('/')
def home():
    return jsonify({'result': 'not found'})

# API 라우팅
@app.route('/api/user/<id>')
def search_users():
    result = []
    for u in users:
        if id == None or int(id) == users[u]["id"]:
            result.append(users[u])
    return jsonify(result)

@app.route('/api/product')
def search_products():
    id = request.args.get('pid')
    name = request.args.get('pname')
    result = []

    for p in products:
        if (id == '' or int(id) == products[p]['id']) and \
           (name == '' or name == products[p]['name']):
            result.append(products[p])

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)