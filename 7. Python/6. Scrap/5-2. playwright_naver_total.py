# bs4
# selenium: 브라우저 제어 -> js를 직접 파싱해서 실행하기엔 오래 걸리므로 브라우저가 대신
# requests: selenium을 사용하면 requests를 사용 안 해도 OK
# playwright: MS가 만듦 -> 가상으로 테스트 자동화가 목적이었으나 웹에도 사용 가능

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://news.naver.com/section/105')

    news = page.locator('.sa_item')
    for i in range(news.count()):
        print(f'{i + 1}번 기사')
        n = news.nth(i)
        title = n.locator('a strong').inner_text()
        print(title)
        link = n.locator('div > div > div.sa_text > a').get_attribute('href')
        print(link)

        page = browser.new_page()
        page.goto(link)
        content = page.locator('#dic_area').all_inner_texts()
        print(content[0].replace('\n', ' '))

        print('-' * 100)