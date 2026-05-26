# flask의 response를 통해 stream event를 줄 수 있음
from flask import Flask, send_from_directory
from flask import request, Response
from queue import Queue

app = Flask(__name__)

# Clients 관리
clients = []

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Server -> Client
# SSE 방식으로 보낼 API
# 이 곳을 통해 메세지를 보낼 때마다 client에게 전달됨 => event-stream
@app.route('/stream')
def stream():
    print('client connected')

    # 파이썬은 함수 내에서 함수 정의 가능
    def event_stream():
        q = Queue()
        clients.append(q) # 응답을 보낼 사용자 목록에 이 새로운 사용자를 추가

        try:
            yield f'data: connected to server\n\n' # 웹 표준 event-stream
            
            while True:
                message = q.get()
                if message is None:
                    break
                yield f'data: {message}\n\n'
        except GeneratorExit:
            print('connection is closed')
        finally:
            clients.remove(q)

    return Response(event_stream(), mimetype='text/event-stream')

# Client -> Server
@app.route('/send', methods=['POST'])
def send():
    message = request.form.get('msg', '')
    print('client message:', message)

    for q in clients:
        q.put(f'server가 받은 message: {message}')
    return ('', 204)

if __name__ == '__main__':
    app.run(threaded=True, debug=False)