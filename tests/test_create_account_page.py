import allure
import pytest
from conftest import create_acc, acc, page
from data.invalid_data import empty_fields, not_equal_passwords


@pytest.mark.smoke
@allure.feature('Smoke')
def test_create_account(create_acc, acc):
    create_acc.open_page(create_acc.page_url)
    acc_info = create_acc.fill_authorization_form()
    create_acc.check_for_success_auth_alert()
    acc.check_for_account_info_equals(*acc_info)


@pytest.mark.regression
@allure.feature('Regression')
@pytest.mark.parametrize('data', empty_fields)
def test_create_account_with_empty_required_fields(create_acc, data):
    first_name, last_name, email, password, password_confirmation = data
    create_acc.open_page(create_acc.page_url)
    create_acc.fill_first_name(first_name)
    create_acc.fill_last_name(last_name)
    create_acc.fill_email(email)
    create_acc.fill_password(password)
    create_acc.fill_password_confirmation(password_confirmation)
    create_acc.click_create_button()
    create_acc.check_for_field_error_messages()


@pytest.mark.regression
@allure.feature('Regression')
@pytest.mark.parametrize('data', not_equal_passwords)
def test_create_account_with_not_equal_passwords(create_acc, data):
    first_name, last_name, email, password, password_confirmation = data
    create_acc.open_page(create_acc.page_url)
    create_acc.fill_first_name(first_name)
    create_acc.fill_last_name(last_name)
    create_acc.fill_email(email)
    create_acc.fill_password(password)
    create_acc.fill_password_confirmation(password_confirmation)
    create_acc.click_create_button()
    create_acc.check_for_password_error_messages()
