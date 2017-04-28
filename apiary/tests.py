from django.test import LiveServerTestCase, TestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep


class Unit(TestCase):

    def test_index_renders_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


    def test_register_node_redirects_if_not_logged_in(self):
        response = self.client.get('/register_node/')
        self.assertRedirects(response, '/login/')


class Functional(LiveServerTestCase):

    def setUp(self):
        self.browser = Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_server_is_available(self):
        self.browser.get(self.live_server_url)
        self.assertIn('home', self.browser.title)

    def test_user_registration_and_node_submission(self):

        # Jesse has at his disposal a cheapo linux sbc and some mediocre python
        # skills. He has a particulate sensor and a nagging suspicion that his
        # building's fire alarms might just be for decoration. He wishes to
        # register the output of his sensor with the array of things project
        # so that he can make this information public and get some sweet
        # visualizations to boot.

        # He is directed to the apiary by some documentation.
        self.browser.get(self.live_server_url)

        # He spies a link that reads 'register a node' and clicks on it!
        self.browser.find_element_by_id('register_a_node').click()
        sleep(0.25)

        # Because he is not logged in, he is redirected to the login page.
        self.assertEqual(self.browser.title, 'Log in')

        # He know he doesn't have an account, so he clicks on the sign-up link.
        self.browser.find_element_by_partial_link_text('Register').click()
        self.assertIn('Register', self.browser.title)

        # He signs up...
        username_input = self.browser.find_element_by_id('id_username')
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password1')
        confirmation_input = self.browser.find_element_by_id('id_password2')

        username_input.send_keys('jesse')
        email_input.send_keys('jesse@email.com')
        password_input.send_keys('testallthethings')
        confirmation_input.send_keys('testallthethings')

        xpath = '//input[@type="submit"]'
        self.browser.find_element_by_xpath(xpath).click()

        # After typing in a username and password, he is forwarded to the
        # node registration process
        self.assertEqual(self.browser.title, 'Register a node')

        # First he is asked information about the features his node reports.
        # Since he doesn't see "gas concentration", he adds his own
        feature_name_input = self.browser.find_element_by_id('feature-name')
        feature_name_input.send_keys('gas_concentration')

        # He also submits the data type values and units of measurement

        # After this, he is asked about the sensor. He puts in the name of the
        # sensor, and what feature its reports map to.

        # From here he is asked to name his node.

        # Because he is not part of any existing network, he is asked to create
        # one. An optional network name is generated for him if he wanted to
        # use it.

        # From there he follows the docs on how to submit his obervations to
        # plenario....
