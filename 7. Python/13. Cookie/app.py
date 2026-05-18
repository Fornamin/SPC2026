from flask import Flask, render_template, make_response, request
app = Flask(__name__)

@app.route('/set-cookie')
def set_cookie():
    res = make_response('Cookie has been set!')
    # 쿠키의 저장소는 브라우저 -> curl로 실행하면 저장 X(쿠키 옵션 줘야함)
    # 쿠키 정보는 헤더에 담김
    res.set_cookie('test-cookie', 'spc2026')
    return res

@app.route('/get-cookie')
def get_cookie():
    cookie = request.cookies.get('test-cookie')
    print(cookie)

    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)