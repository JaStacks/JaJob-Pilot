from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
from login import login_logic
# Load environment variables from .env.json


def main():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch_persistent_context(user_data_dir='./user_data', # Store persistent context
                                                        headless=False)  # Keep headless=False to see what's happening

        # Call login logic function
        login_logic(browser)

        # Use authenticated context to access the desired page
        page = browser.new_page()
        page.goto("https://app.joinhandshake.com/career_fairs/50357/employers_list?ajax=true&query=&category=StudentRegistration&page=2&per_page=25&sort_direction=asc&sort_column=default&followed_only=false&qualified_only=&core_schools_only=false&including_all_facets_in_searches=true")

        # Take a screenshot
        page.screenshot(path="screenshot.jpg", full_page=True)

        # Extract content and parse with BeautifulSoup
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        with open("content.html", "w", encoding='utf-8') as f:
            f.write(soup.prettify())

        # Close browser
        input("Enter to close browser")
        browser.close()

if __name__ == "__main__":

    main()