from django.test import Client
from django.urls import reverse

import unittest

# Create your tests here.

class TopPageTest(unittest.TestCase):
    def test_show_top_page(self):
        client = Client()
        response = client.get(reverse('GroupConnect:index'))
        self.assertEqual(
            response.status_code,
            200
        )
