from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep


class Functional(LiveServerTestCase):

    def setUp(self):
        self.browser = Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_server_is_available(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Api Root', self.browser.title)
