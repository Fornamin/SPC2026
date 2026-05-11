# 외부 module -> pypi.org에서 확인 가능 / install 필요
# https://requests.readthedocs.io/en/latest/
# 가상 환경에 설치
import requests 

# 외부에 HTTP 요청을 대신 해주는 라이브러리
res = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# 응답 코드
print(res.status_code)
# 웹 페이지 내용
print(res.text)

res = requests.get('https://api.github.com')
if res.status_code == 200:
    print(res.text)
else:
    print('failed to load page / code: ', res.status_code)