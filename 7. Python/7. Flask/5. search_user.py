from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'John', 'age': 28, 'phone': '010-1234-5678'},
    {'name': 'Emma', 'age': 31, 'phone': '010-2345-6789'},
    {'name': 'Michael', 'age': 25, 'phone': '010-3456-7890'},
    {'name': 'Olivia', 'age': 34, 'phone': '010-4567-8901'},
    {'name': 'James', 'age': 29, 'phone': '010-5678-9012'},
    {'name': 'Sophia', 'age': 27, 'phone': '010-6789-0123'},
    {'name': 'Daniel', 'age': 40, 'phone': '010-7890-1234'},
    {'name': 'Ava', 'age': 22, 'phone': '010-8901-2345'},
    {'name': 'Ethan', 'age': 36, 'phone': '010-9012-3456'},
    {'name': 'Mia', 'age': 30, 'phone': '010-0123-4567'},
    {'name': 'Elen', 'age': 28, 'phone': '010-1122-3344'},
    {'name': 'Lucas', 'age': 33, 'phone': '010-2233-4455'},
    {'name': 'Charlotte', 'age': 26, 'phone': '010-3344-5566'},
    {'name': 'Benjamin', 'age': 41, 'phone': '010-4455-6677'},
    {'name': 'Amelia', 'age': 24, 'phone': '010-5566-7788'},
    {'name': 'Henry', 'age': 37, 'phone': '010-6677-8899'},
    {'name': 'Harper', 'age': 32, 'phone': '010-7788-9900'},
    {'name': 'Alexander', 'age': 45, 'phone': '010-8899-0011'},
    {'name': 'Ella', 'age': 23, 'phone': '010-9900-1122'},
    {'name': 'Sebastian', 'age': 38, 'phone': '010-1010-2020'},
    {'name': 'Grace', 'age': 29, 'phone': '010-2020-3030'},
    {'name': 'Jack', 'age': 27, 'phone': '010-3030-4040'},
    {'name': 'Lily', 'age': 35, 'phone': '010-4040-5050'},
    {'name': 'David', 'age': 42, 'phone': '010-5050-6060'},
    {'name': 'Chloe', 'age': 21, 'phone': '010-6060-7070'},
    {'name': 'Matthew', 'age': 39, 'phone': '010-7070-8080'},
    {'name': 'Zoe', 'age': 28, 'phone': '010-8080-9090'},
    {'name': 'Joseph', 'age': 34, 'phone': '010-9090-1010'},
    {'name': 'Nora', 'age': 26, 'phone': '010-1111-2222'},
    {'name': 'Samuel', 'age': 31, 'phone': '010-2222-3333'},
    {'name': 'Hannah', 'age': 25, 'phone': '010-3333-4444'}
]

@app.route('/users')
def search_user():
    # query param으로 나이나 이름이나 전화번호를 받아서 서치 -> 결과 반환
    result = []

    name = request.args.get('name', type=str)
    age = request.args.get('age', type=int)
    phone = request.args.get('phone', type=str)

    for u in users:
        if ((name == None or name.lower() == u['name'].lower()) and \
            (age == None or age == u['age']) and \
            (phone == None or u['phone'].startswith(phone))):
            result.append(u)
        
    return result

if __name__ == '__main__':
    app.run(debug=True)