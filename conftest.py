from playwright.sync_api import BrowserContext
import pytest

from generator.generator import generated_user
from pages.account_page import MyAccount
from pages.create_account_page import CreateAccountPage
from pages.eco_page import EcoFriendlyPage
from pages.login_page import LoginPage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page
    page.close()


@pytest.fixture()
def create_acc(page):
    return CreateAccountPage(page)


@pytest.fixture()
def acc(page):
    return MyAccount(page)


@pytest.fixture()
def login(page):
    return LoginPage(page)


@pytest.fixture()
def eco(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def create_user(page, create_acc):
    user = next(generated_user())
    create_acc.open_page(create_acc.page_url)
    create_acc.fill_first_name(user.first_name)
    create_acc.fill_last_name(user.last_name)
    create_acc.fill_email(user.email)
    create_acc.fill_password(user.password)
    create_acc.fill_password_confirmation(user.confirm_password)
    create_acc.click_create_button()
    create_acc.check_for_success_auth_alert()
    print(user.email)
    print(user.password)
    return user.email, user.password
