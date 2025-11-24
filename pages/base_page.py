from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Навігація на URL"""
        self.page.goto(url, wait_until="domcontentloaded")

    def click (self, locator: str):
        self.page.wait_for_selector(locator, state="visible")
        self.page.click(locator)



