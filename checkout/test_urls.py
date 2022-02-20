# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Internal
from .views import checkout, checkout_success, cache_checkout_data, webhook
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutUrls(SimpleTestCase):
    """
    Tests brand urls are resolved
    to the brand views.
    """
    def test_brand_url_resolves(self):
        """
        Checks main checkout url is resolved
        """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url_resolves(self):
        """
        Checks checkout_success url is resolved with args
        """
        url = reverse('checkout_success', args=[1])
        self.assertEqual(resolve(url).func, checkout_success)

    def test_cache_checkout_url_resolves(self):
        """
        Checks edit_brand url is resolved with args
        """
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)

    def test_webhook_url_resolves(self):
        """
        Checks webhook url is resolved
        """
        url = reverse('wh', args=['nike'])
        self.assertEqual(resolve(url).func, webhook)
