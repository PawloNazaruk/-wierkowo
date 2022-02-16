from django.test import TestCase
from pprint import pprint
from selenium import webdriver


class UnitTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_home_page_exist(self):
        self.browser.get('http://localhost:8080/home')
        self.assertIn('Świerkowo', self.browser.page_source)
        pprint(self.browser.page_source)
        pprint(self.browser)

    def tearDown(self):
        self.browser.quit()
