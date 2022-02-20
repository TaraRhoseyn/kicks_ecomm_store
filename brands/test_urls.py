# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.test import TestCase, Client
from django.urls import reverse, resolve


# Internal
from .views import add_brand, show_brand, edit_brand, delete_brand
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestBrandUrls(TestCase):
    """
    Tests brand urls are resolved
    to the brand views.
    """
    def test_brand_url_resolves(self):
        """
        Checks main brand url is resolved
        """
        response = self.client.get('/brands/')
        self.assertEqual(response.status_code, 200)

    def test_add_brand_url_resolves(self):
        """
        Checks add_brand url is resolved
        """
        url = reverse('add_brand')
        self.assertEqual(resolve(url).func, add_brand)

    def test_adjust_brand_url_resolves(self):
        """
        Checks edit_brand url is resolved with args
        """
        url = reverse('edit_brand', args=['nike'])
        self.assertEqual(resolve(url).func, edit_brand)
    
    def test_delete_brand_url_resolves(self):
        """
        Checks delete_brand url is resolved with args
        """
        url = reverse('delete_brand', args=['nike'])
        self.assertEqual(resolve(url).func, delete_brand)
