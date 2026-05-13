from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)

    result = f'Your Query is {query}, Page is {page}'
    return jsonify({'msg': result})

@app.route('/user/<username>/post')
def show_user_posts(username):
    page = request.args.get('page', default=1, type=int)
    result = f'User is {username} and page is {page}'

    return jsonify({'msg': result})

if __name__ == '__main__':
    app.run(debug=True)