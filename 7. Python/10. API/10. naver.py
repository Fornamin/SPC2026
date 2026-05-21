import requests

from dotenv import load_dotenv
import os

load_dotenv()

text = '생성형 ai'
blog_url = 'https://openapi.naver.com/v1/search/blog.json'
news_url = 'https://openapi.naver.com/v1/search/news.json'

headers = {
    'X-Naver-Client-Id': os.getenv('Naver_ClIENT_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_CLIENT_SECRET')
}
params = {
    'query': text
}

res = requests.get(news_url, headers=headers, params=params)
data = res.json()

print(data)