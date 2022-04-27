from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestPageLoad(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())
