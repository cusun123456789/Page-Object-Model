from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestSignUpPage(BaseTest):
    def test_sign_up_button(self):
        print("\n" + str(test_cases(2)))
        page = SignUpBasePage(self.driver)
        sign_up_page = page.click_sign_up_button()
        self.driver.save_screenshot('BeforeSingUp.png')
        self.driver.find_element_by_id("ap_customer_name").send_keys("congquyet0808")
        self.driver.find_element_by_id("ap_email").send_keys("quyet49022@donga.edu.vn")##lỗi chỗ này em chưa tìm ra
        self.driver.find_element_by_id("ap_password").send_keys("quyet2k1")
        self.driver.find_element_by_id("ap_password_check").send_keys("quyet2k1")
        self.driver.find_element_by_id("continue").click()
        self.assertIn("ap/register", sign_up_page.get_url())
        self.driver.save_screenshot('AfterSingUp.png')
