from django.test import TestCase


class Views(TestCase):

    def test_index_returns_custom_homepage(self):
        response = self.client.get('/')

        self.assertIn(b'Welcome!', response.content)