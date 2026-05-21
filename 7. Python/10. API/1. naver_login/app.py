from flask import Flask, render_template, redirect, request, session, url_for
import requests

from dotenv import load_dotenv
import os

load_dotenv()
cliet_id = os.getenv('NAVER_CLIENT_ID')
callback_url = os.getenv('NAVER_REDIRECT_URI')
client_secret = os.getenv('NAVER_CLIENT_SECRET')

app = Flask(__name__)
app.secret_key = os.getenv('MY_SESSION_KEY')

# 이 부분을 BluePrint로 관리하면 좋음
naver_token_url = 'https://nid.naver.com/oauth2.0/token'
naver_auth_url = 'https://nid.naver.com/oauth2.0/authorize'
naver_profile_url = 'https://openapi.naver.com/v1/nid/me'

@app.route('/')
def index():
        user = session.get('user')
        return render_template('index.html', user=user)

@app.route('/login')
def naver_login():
    # 최초로 인증하는 주소
    auth_url = (
                f'{naver_auth_url}?'
                f'response_type=code&client_id={cliet_id}'
                f'&redirect_uri={callback_url}&state=HELLO'
        )
    return redirect(auth_url)

@app.route('/api/naver/callback')
def naver_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    # 내가 확인하는 주소
    token_url = (
                f'{naver_token_url}?'
                f'grant_type=authorization_code&client_id={cliet_id}'
                f'&client_secret={client_secret}&code={code}&state={state}'
        )
    token_res = requests.get(token_url).json()
    access_token = token_res.get('access_token')
    print(access_token)

    # 내가 정보 요청하는 주소
    headers = {'Authorization': f'Bearer {access_token}'}
    profile = requests.get(naver_profile_url, headers=headers).json()
    print('user info: ', profile)

    session['user'] = profile['response']

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)