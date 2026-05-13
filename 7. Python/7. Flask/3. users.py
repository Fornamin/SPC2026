from flask import Flask, jsonify

app = Flask(__name__)

users = [ # python의 list -> 안에는 dict
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
    {'name': 'Elen', 'age': 28, 'phone': '010-8901-2345'}
]

@app.route('/')
def show_users(): 
    return jsonify(users)

@app.route('/users/<name>')
def get_user_by_name(name): 
    print('input:', name)
    user = None
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
    if user:
        return jsonify(user)
    else:
        return '<h1>Not Found</h1>'

@app.route('/users/<int:age>')
def get_user_by_age(age):
    user = []
    for u in users:
        if u['age'] == age:
            user.append(u)

    if user:
        return jsonify(user)
    else:
        return jsonify({'msg':'Not Found'})

if __name__ == '__main__':
    app.run(debug=True)