from bs4 import BeautifulSoup
import requests
import csv

# bs4
# selenium: 브라우저 제어 -> js를 직접 파싱해서 실행하기엔 오래 걸리므로 브라우저가 대신
# requests: selenium을 사용하면 requests를 사용 안 해도 OK
# playwright: MS가 만듦 -> 가상으로 테스트 자동화가 목적이었으나 웹에도 사용 가능

url = 'https://www.naver.com/'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

news = soup.select('#newsstand > div.MediaView-module__media_area___Z4js3')
print(news)

# books = soup.select('article.product_pod')
# books_dict = []
# rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# for book in books:
#     books_dict.append({'Title': book.h3.a['title'], \
#                        'Price': book.find_all('div')[1].p.text, \
#                         'Rating': rating_map[book.p['class'][1]]})

# with open('7. Python/File/bookscrap-get-prof.csv', 'w', encoding='utf-8', newline='') as file:
#     csv_writer = csv.DictWriter(file, fieldnames = ['Title', 'Price', 'Rating'])
#     csv_writer.writeheader() # 첫 줄에 header 추가
#     csv_writer.writerows(books_dict)