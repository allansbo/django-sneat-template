from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestHome(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r('core:home'))

    def test_get(self):
        """Get / must return status_code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Get / must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
