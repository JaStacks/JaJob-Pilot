import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def login_logic(page):
    # Load environment variables from .env.json using json.loads
    with open('.env.json', 'r') as f:
        raw_data = f.read()
        env = json.loads(raw_data)  # Correctly parse JSON data to a dictionary

    # Go to the login page
    page.goto("https://app.joinhandshake.com/login")

    # Click to open the dropdown for school selection
    page.click("div.select2-container")  # Click the dropdown to reveal the list

    # Wait for the dropdown list to be visible
    page.wait_for_selector("div.select2-drop-active", state="visible")

    # Type the school name to filter the dropdown list
    school_name = "University of California‚ Irvine"  # Update this value as needed
    page.fill('input.select2-input', school_name)

    # Wait for the filtered list to be populated
    page.wait_for_selector("ul.select2-results li")

    # Select the specific school
    page.click(f"div.select2-result-label:has-text('{school_name}')")
    page.wait_for_selector("a.sso-button", timeout=60000)
    page.click("a.sso-button")

    # Wait for redirection to the Duo login page
    page.wait_for_selector('input#j_username', timeout=60000)

    # Fill in the Duo authentication form
    page.fill('input#j_username', env['username'])  # Fill in UCInetID
    page.fill('input#j_password', env['password'])  # Fill in Password

    # Click the login button
    page.click('input[type="submit"][name="submit_form"]')

    # Wait for Duo authentication step to complete
    input("Please complete Duo authentication in the opened browser, then press Enter...")

    # Save authentication state after successful login
    page.context.storage_state(path='auth.json')

    return page  # Return the page object for further use if needed