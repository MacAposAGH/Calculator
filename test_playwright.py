"""Tests for playwright.py"""

import pytest
from playwright.sync_api import Page, expect, Locator

def click_link(page: Page | Locator, name:str, exact:bool = False):
    """Click link"""
    page.get_by_role("link", name=name, exact=exact).click()

class TestPlaywright:
    """Tests for playwright.py"""

    @pytest.fixture(autouse=True)
    def open_agh_website(self, page: Page):
        """Open website before each test"""
        page.goto("https://www.informatyka.agh.edu.pl/pl/")

    def test_open(self, page: Page):
        """Test whether the website opens correctly"""
        response = page.goto("https://www.informatyka.agh.edu.pl/pl/")
        assert response is not None
        assert response.status == 200
        assert page.title() != ""

    def test_subpage_header(self, page: Page):
        """Test subpage header"""
        click_link(page,"Wydział", True)
        click_link(page,"O Wydziale")
        expect(
            page.get_by_role("heading", name="O Wydziale")
        ).to_be_visible()

    def test_subpage_content(self, page: Page):
        """Test subpage content"""
        page.get_by_role("link", name="Kandydaci").click()
        click_link(page.locator("#studenci-dla-kandydatow-kierunki"), "Nasze kierunki")
        expect(
            page.get_by_role("heading", name="Nasze kierunki")
        ).to_be_visible()

    def test_url(self, page: Page):
        """Test url"""
        click_link(page, "Studenci")
        click_link(page, "Koła naukowe")
        expect(page).to_have_url(
            "https://www.informatyka.agh.edu.pl/pl/studenci/wiecej-niz-studia/")
