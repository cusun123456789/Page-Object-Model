from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestSearchPage(BaseTest):
    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        self.driver.save_screenshot('BeforeSearch.png')
        search_result = page.search_item("samsung")
        self.assertIn("samsung", search_result)
        self.driver.save_screenshot('AfterSearch.png')