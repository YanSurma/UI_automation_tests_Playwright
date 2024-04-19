from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url):
        return self.page.goto(self.base_url + self.page_url)

    def find(self, locator) -> Locator:
        return self.page.locator(locator)