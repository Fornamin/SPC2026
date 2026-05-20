from flask import Flask, send_from_directory, jsonify, request
from database import MyDatabase

app = Flask(__name__)
db = MyDatabase()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()

    sql = 'INSERT INTO board (title, message) VALUES(?, ?)'
    db.execute(sql, (data['title'], data['content']))
    db.commit()

    return jsonify({'result': 'success'})

@app.route('/list')
def list():
    result = db.execute_fetch('SELECT * FROM board')
    dict_result = [{'id': r['id'], 'title': r['title'], 'message': r['message']}
                   for r in result]
    return jsonify(dict_result)

@app.route('/delete', methods=['POST'])
def delete():
    return jsonify({'result': 'success'})

@app.route('/modify', methods=['POST'])
def modify():
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)