from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as p:

    browser = p.chromium.launch()
    context = browser.new_context(

        user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    )

    page = context.new_page()
    page.goto("https://app.joinhandshake.com/career_fairs/50357/employers_list?ajax=true&query=&category=StudentRegistration&page=2&per_page=25&sort_direction=asc&sort_column=default&followed_only=false&qualified_only=&core_schools_only=false&including_all_facets_in_searches=true")
    page.fill('input#email-address-identifier', env.username);
    page.screenshot(path="screenshot.jpg", full_page=True)

    content = page.content()

    soup = BeautifulSoup(content, "html.parser")
    with open("content.html", "w",encoding='utf-8') as f:

        f.write(soup.prettify())

    browser.close()
    