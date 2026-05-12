from bs4 import BeautifulSoup
import requests

url = 'https://www.naver.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.find('title')
print(title)

headings = soup.find_all('h1')
print(headings)

divs = soup.find_all('div')
for e in divs:
    link = e.a # element 중 a 태그를 가진 것을 찾기
    if link:
        href = link.get('href')
        print(f'link: {href}')