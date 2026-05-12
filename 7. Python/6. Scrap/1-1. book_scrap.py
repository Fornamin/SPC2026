# 1. https://books.toscrape.com/에 접속해서 페이지 받아오기
# 2. DOM을 bs4로 구현
# 3. 도서들의 이름, 평점, 가격을 받아오기
# 4. csv로 만들기

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://books.toscrape.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title_list = []

price_list = []
books_price = soup.find_all('p', class_='price_color')
for book in books_price:
    price = book.text.replace('Â£', '').strip()
    price_list.append(price)

rating_list = []
books_star = soup.find_all('article', class_='product_pod')
for book in books_star:
    title_list.append(book.h3.a.get('title'))
    rating_list.append(book.p.attrs.get('class')[1])

data = []
for i in range(len(title_list)):
    data.append([title_list[i], price_list[i], rating_list[i]])

with open('7. Python/File/bookscrap-get.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Title', 'Price', 'Rating'])
    csv_writer.writerows(data)