from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *


class HelpPage(BasePage):

    def __init__(self, driver):
        self.locator = HelpPageLocators
        super(HelpPage, self).__init__(driver)

    def enter_search_question(self, question):
        self.find_element(*self.locator.HELPSEARCH).send_keys(question)
        self.find_element(*self.locator.HELPSEARCH).send_keys(Keys.ENTER)

    def get_text_result(self):
        paymentText = self.find_element(*self.locator.PAYMENTMETHODTEXT)
        return paymentText
