from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.help_page import HelpPage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *


# Đối tượng trang được viết trong mô-đun này.
# Tùy thuộc vào chức năng của trang, chúng ta có thể có nhiều chức năng hơn cho các lớp mới
class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def navigate_help_page(self):
        self.find_element(*self.locator.HELP_LINK).click()
        return HelpPage(self.driver)


    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpBasePage(self.driver)

    def click_sign_in_button(self):
        self.find_element(*self.locator.LOGIN).click()

        return LoginPage(self.driver)
