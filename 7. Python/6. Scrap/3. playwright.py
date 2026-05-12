from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # lauch chrome
    browser = p.chromium.launch(headless=False)
    # 빈 페이지
    page = browser.new_page()
    # 원하는 사이트로 가기
    page.goto('https://www.naver.com')
    print(page.title())
    page.screenshot(path='naver.png')
    input('Enter -> 종료')