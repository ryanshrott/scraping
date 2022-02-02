import sys

from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    url = "https://www.airbnb.ca/rooms/48058366"
    page.goto(url)
    page.wait_for_timeout(10000)

    browser.close()