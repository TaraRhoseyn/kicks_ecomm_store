# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Internal
from .views import add_brand, brands, edit_brand, delete_brand
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestBrandUrls(SimpleTestCase):
    """
    Tests brand urls are resolved
    to the brand views.
    """
    def test_brand_url_resolves(self):
        url = reverse('show_brand')
        self.assertEqual(resolve(url).func, brands)

    def test_add_brand_url_resolves(self):
        url = reverse('add_brand', args=['nike'])
        self.assertEqual(resolve(url).func, add_brand)
    
    def test_adjust_brand_url_resolves(self):
        url = reverse('edit_brand', args=['nike'])
        self.assertEqual(resolve(url).func, edit_brand)
    
    def test_remove_brand_url_resolves(self):
        url = reverse('delete_brand', args=['nike'])
        self.assertEqual(resolve(url).func, delete_brand)
