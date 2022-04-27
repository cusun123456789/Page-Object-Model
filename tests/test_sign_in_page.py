
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestSignInPage(BaseTest):

    def test_sign_in_button(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.driver.save_screenshot('BeforeSingIn.png')
        self.driver.find_element_by_id("ap_email").send_keys("congquyet0808@gmail.com")
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("ap_password").send_keys("quyet2k1")
        self.driver.find_element_by_id("signInSubmit").click()
        self.assertIn("ap/signin", login_page.get_url())
        self.driver.save_screenshot('AfterSingIn.png')

