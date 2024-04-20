from time import sleep

from conftest import login


def test_login(login):
    login.open_page(login.page_url)
    login.fill_email('qa1_user@gmail.com')
    login.fill_password('IGyVWvsJsQsmuC^b')
    login.click_sign_in_button()
    login.check_page_title('My Account')

    # без заполнения email

    # без заполнения password

    # не существующий пользователь

    # методы на проверку ошибок
