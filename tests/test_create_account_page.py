from time import sleep

import pytest

from conftest import create_account
from data.invalid_data import empty_fields, not_equal_passwords
from generator.generator import generated_user


def test_create_account(create_account):
    create_account.open_page(create_account.page_url)
    create_account.fill_authorization_form()
    create_account.check_for_success_auth_alert()


@pytest.mark.parametrize('data', empty_fields)
def test_create_account_with_empty_required_fields(create_account, data):
    create_account.open_page(create_account.page_url)
    create_account.fill_first_name(data[0])
    create_account.fill_last_name(data[1])
    create_account.fill_email(data[2])
    create_account.fill_password(data[3])
    create_account.fill_password_confirmation(data[4])
    create_account.click_create_button()
    create_account.check_for_field_error_messages()


@pytest.mark.parametrize('data', not_equal_passwords)
def test_create_account_with_not_equal_passwords(create_account, data):
    create_account.open_page(create_account.page_url)
    create_account.fill_first_name(data[0])
    create_account.fill_last_name(data[1])
    create_account.fill_email(data[2])
    create_account.fill_password(data[3])
    create_account.fill_password_confirmation(data[4])
    create_account.click_create_button()
    create_account.check_for_password_error_messages()
