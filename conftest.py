from playwright.sync_api import BrowserContext
import pytest

from pages.create_account_page import CreateAccountPage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account(page):
    return CreateAccountPage(page)
