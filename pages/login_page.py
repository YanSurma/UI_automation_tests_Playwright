from pages.base_page import BasePage
from pages.locators import login_page_locators as loc


class LoginPage(BasePage):
    page_url = '/customer/account/login'

    # IGyVWvsJsQsmuC^b  \ qa1_user@gmail.com

    def fill_email(self, email_value):
        email_field = self.find(loc.EMAIL_FIELD)
        email_field.fill(email_value)

    def fill_password(self, passw_value):
        email_field = self.find(loc.PASSWORD_FIELD)
        email_field.fill(passw_value)

    def click_sign_in_button(self):
        sign_in_button = self.find(loc.SIGN_IN_BUTTON)
        sign_in_button.click()
