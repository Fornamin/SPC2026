# pip install flask-sock
from flask import Flask, send_from_directory
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@sock.route('/ws')
def websocket(ws):
    print('connected to client')
    ws.send('connected to server')

    while True:
        try:
            msg = ws.receive()
            print('client msg:', msg)

            ws.send(f'message: {msg}')
        except Exception as e:
            print('error:', e)
            break
    print('close to connection')

if __name__ == '__main__':
    app.run(debug=True)