from flask import Flask, request
from flask import render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # Flask나 SQLAlchemy와는 무관
    # 파이썬 클래스를 출력할 때 출력 포맷을 커스텀해서 정의
    def __repr__(self):
        return f'<User {self.id}> {self.name}, {self.age}'
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-alchemy-test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB(SQLAlchemy)와 Flask를 연동
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    for user in users:
        print(user)
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')

    if not name or not age:
        flash('Enter both name and age')
        return redirect(url_for('index'))
    
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_user/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)

    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f'User(Id: {id}) is deleted')

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        print('Database init . . .')
        db.create_all()

        if not User.query.first():
            print('Users init . . .')
            user1 = User(name='kim', age=22)
            user2 = User(name='lee', age=26)
            user3 = User(name='park', age=34)

            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
            db.session.commit()

    app.run(debug=True)