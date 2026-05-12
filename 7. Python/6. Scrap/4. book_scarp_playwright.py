from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://books.toscrape.com/')

    books = page.locator('article.product_pod')
    for i in range(books.count()):
        book = books.nth(i)
        title = book.locator('h3 a').get_attribute('title')
        price = book.locator('.price_color').inner_text().replace('£', '')
        rating = book.locator('p.star-rating').get_attribute('class').split()[1]