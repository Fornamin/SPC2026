# bs4
# selenium: 브라우저 제어 -> js를 직접 파싱해서 실행하기엔 오래 걸리므로 브라우저가 대신
# requests: selenium을 사용하면 requests를 사용 안 해도 OK
# playwright: MS가 만듦 -> 가상으로 테스트 자동화가 목적이었으나 웹에도 사용 가능

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.naver.com/')

    books = page.locator('article.product_pod')
    # for i in range(books.count()):
    #     book = books.nth(i)
    #     title = book.locator('h3 a').get_attribute('title')
    #     price = book.locator('.price_color').inner_text().replace('£', '')
    #     rating = book.locator('p.star-rating').get_attribute('class').split()[1]