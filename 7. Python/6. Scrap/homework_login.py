from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# browser
#  └── context (쿠키 저장소)
#       ├── page 1 (shop)
#       ├── page 2 (detail)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://makemyproject.net/shop/')

    # Login
    page.fill('#uid', 'user123')
    page.fill('#upw', 'password1234')
    page.click('#loginBtn')
    page.wait_for_timeout(2000)

    who = page.locator('#who').inner_text()
    print(who)

    # Page
    pager_buttons = page.locator('#pager button')
    total_pages = pager_buttons.count()

    for current_page in range(total_pages):
        # 페이지 이동
        if current_page > 0:
            pager_buttons.nth(current_page).click()
        page.locator('#products .card').first.wait_for()    
        print(f'PAGE {current_page + 1}')
        product_info = page.locator('#products > .card')
        print('Product Count: ', product_info.count())

        for i in range(product_info.count()):
            product = product_info.nth(i)

            member = product.locator('span').nth(0).inner_text()
            name = product.locator('a').inner_text()
            id = name.split('#')[1]
            price = product.locator('strong').inner_text().split(': ')[1]
            content = product.locator('.muted').nth(0).inner_text()

            # 상세 페이지
            page_product = context.new_page()
            page_product.goto(f'https://makemyproject.net/shop/products/{id}')

            print(f'[{member}] Product: {name}\nPrice: {price}, Content: {content}')

            page_product.wait_for_selector('.review', timeout=10000)
            review_info = page_product.locator('.review')
            for j in range(review_info.count()):
                review = review_info.nth(j)
                print(f'Review #{j + 1} {review.locator('b').inner_text()}')
                print(f'{review.locator('div').inner_text()}')
            print('-' * 100)