from flask import Flask, render_template, make_response, request
app = Flask(__name__)

# curl 127.0.0.1:5000/-c session.txt -b session.txt

@app.route('/')
def main():
    cookie = request.cookies.get('test-cookie')

    if cookie:
        return f'You already have Cookie: {cookie}'
    
    res = make_response('Cookie has been set!')
    res.set_cookie('test-cookie', 'spc2026')

    # 헤더를 반환해야
    return res

if __name__ == '__main__':
    app.run(debug=True)