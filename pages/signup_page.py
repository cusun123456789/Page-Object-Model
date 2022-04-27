from pages.base_page import BasePage
from utils.locators import SingUpLocators


class SingupPage:
    pass


class SignUpBasePage(BasePage):
    def click_sign_up_button(self):
        pass

    def __init__(self, driver):
        self.locator = SingUpLocators
        super(SingupPage, self).__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_sing_up_button(self):
        self.find_element(*self.locator.SUBMIT).click()
