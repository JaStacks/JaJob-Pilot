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

    # Fill in the email field
    page.fill('input#email-address-identifier', env['username'])

    # Authenticity token handling (assuming dynamic value)
    authenticity_token = page.get_attribute('input[name="authenticity_token"]')
    if authenticity_token:
        page.fill('input[name="authenticity_token"]', authenticity_token)
    
    # Click on the submit button to proceed with login
    page.click('button[type="submit"]')

    # Wait for navigation or Duo authentication page
    input("Please complete Duo authentication in the opened browser, then press Enter...")

    # Save authentication state after successful login
    page.context.storage_state(path='auth.json')

    return page  # Return the page object for further use if needed