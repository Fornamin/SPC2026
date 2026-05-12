import requests

url = 'https://www.example.com'
res = requests.get(url)
html = res.text # http 프로토콜 응답 결과 -> html
print(html)

# find tags what you want
start = html.find('<h1>')
end = html.find('</h1>')
text = html[start:end + 5]
print(text)
text = html[start + 4:end]
print(text)

# bs4(beautifulsoup4)