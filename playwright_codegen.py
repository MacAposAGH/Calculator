"""Playwright codegen"""
from playwright.sync_api import Playwright, sync_playwright

def run(playwright_manager: Playwright) -> None:
    """Run playwright"""
    browser = playwright_manager.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.informatyka.agh.edu.pl/pl/")
    page.get_by_role("link", name="O Wydziale").click()
    page.locator("div").filter(has_text="HISTORIA Historia rozwoju").nth(2).click()
    page.get_by_role("link", name="Strona główna").click()
    page.locator("div").filter(has_text="Dydaktyka").nth(3).click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
