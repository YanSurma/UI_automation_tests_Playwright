import allure
import pytest

from conftest import login, page


# @pytest.mark.smoke
@allure.feature('Smoke')
def test_login(login):
    login.open_page(login.page_url)
    login.fill_email('qa1_user@gmail.com')
    login.fill_password('IGyVWvsJsQsmuC^b')
    login.click_sign_in_button()
    login.check_page_title('My Account')


@pytest.mark.regression
@allure.feature('Regression')
def test_login_with_empty_email(login):
    login.open_page(login.page_url)
    login.fill_email('')
    login.fill_password('IGyVWvsJsQsmuC^b')
    login.click_sign_in_button()
    login.check_for_email_error()


@pytest.mark.regression
@allure.feature('Regression')
def test_login_with_empty_password(login):
    login.open_page(login.page_url)
    login.fill_email('qa1_user@gmail.com')
    login.fill_password('')
    login.click_sign_in_button()
    login.check_for_password_error()


@pytest.mark.regression
@allure.feature('Regression')
def test_login_non_exists_user(login):
    login.open_page(login.page_url)
    login.fill_email('example@example.com')
    login.fill_password('examplepa$$w0rd')
    login.click_sign_in_button()
    login.check_for_login_error()
