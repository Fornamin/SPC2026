from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>간단한 HTML</title>
</head>
<body>
    <h1>안녕하세요 👋</h1>
    <p>이것은 간단한 HTML 예제입니다.</p>
    <p>first</p>
    <p>second</p>
    <p>third</p>
    <button onclick="sayHello()">
        클릭하기
    </button>
    <script>
        function sayHello() {
            alert("Hello!");
        }
    </script>
</body>
</html>'''
soup = BeautifulSoup(html, 'html.parser')
print(soup)

header = soup.find_all('h1') # html 안의 모든 h1 태그
paragraph = soup.find_all('p') # html 안의 모든 p 태그
print(header)
print(paragraph)