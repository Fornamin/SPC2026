from flask import Flask

app = Flask(__name__)

@app.route('/user')
@app.route('/user/<username>') # 가변 인자
def show_user_profile(username = 'Annonymous'):
    return f'<h1>User: {username}</h1>'

@app.route('/admin')
def show_admin_profile():
    return 'Admin: Min'

@app.route('/product')
@app.route('/product/<int:id>') # id를 int형으로 지정
def show_product_profile(id = -1):
    return f'<h1>Product Code: {id}, Product: Pepsi</h1>'

if __name__ == '__main__':
    app.run(debug=True) # True 값을 주면 저장할 때마다 자동으로 재실행
