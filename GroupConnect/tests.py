from django.test import client
from django.urls import reverse

import unittest

# Create your tests here.

class TopPageTest(unittest.TestCase):
    def test_show_top_page(self):
        response = self.client.get('GroupConnect:index')
        self.assertEqual(
            response.status_code,
            200
        )
