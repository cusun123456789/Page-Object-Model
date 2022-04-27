from pages.help_page import HelpPage
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases



class TestHelpPage(BaseTest):

    def test_search_help_question(self):
        # Step01: Navigate to Help Page
        page = MainPage(self.driver)
        helpPage = page.navigate_help_page()

        # Step02: Enter 'payment' into search text box
        helpPage.enter_search_question('payment method')

        # Step03: Verify the return result
        paymentText = helpPage.get_text_result()
        self.assertIsNotNone(paymentText)
