from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://makemyproject.net/shop/')

    # js가 데이터를 생성하기 전에 호츨하면 데이터를 못 받아옴
    page.wait_for_selector('.card', timeout=10000)
    head = page.locator('#products > .card')
    print('Product Count: ', head.count())

    for i in range(head.count()):
        product = head.nth(i)

        name = product.locator('a').inner_text()
        id = name.split('#')[1]
        price = product.locator('strong').inner_text()
        content = product.locator('.muted').nth(0).inner_text()

        print(f'Product: {name}\nPrice: {price}, Content: {content}')
        print('-' * 50)