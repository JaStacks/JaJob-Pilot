from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:

    browser = p.chromium.launch()
    context = browser.new_context(

        user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    )

    page = context.new_page()
    page.goto("https://www.indeed.com/jobs?q=&l=irvine%2C%20ca&from=searchOnHP")
    page.screenshot(path="screenshot.jpg", full_page=True)

    content = page.content()

    soup = BeautifulSoup(content, "html.parser")
    with open("content.html", "w",encoding='utf-8') as f:

        f.write(soup.prettify())

    browser.close()
    