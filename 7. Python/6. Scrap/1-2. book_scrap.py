from bs4 import BeautifulSoup
import requests
import csv

url = 'https://books.toscrape.com/'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

books = soup.select('article.product_pod')
books_dict = []
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

for book in books:
    books_dict.append({'Title': book.h3.a['title'], \
                       'Price': book.find_all('div')[1].p.text, \
                        'Rating': rating_map[book.p['class'][1]]})

with open('7. Python/File/bookscrap-get-prof.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames = ['Title', 'Price', 'Rating'])
    csv_writer.writeheader() # 첫 줄에 header 추가
    csv_writer.writerows(books_dict)