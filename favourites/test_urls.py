# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Internal
from .views import view_favourites, add_product_to_favourites

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestFavouritesUrls(SimpleTestCase):
    """
    Tests favourites urls are resolved
    to the favourites views.
    """

    def test_view_favourite_url_resolves(self):
        """
        Checks view_favourites url is resolved with args
        """
        url = reverse('view_favourites')
        self.assertEqual(resolve(url).func, view_favourites)
    
    def test_add_product_to_favourites_resolves(self):
        """
        Checks add_product_to_favourites url is resolved
        """
        url = reverse('add_product_to_favourites', args=['1'])
        self.assertEqual(resolve(url).func, add_product_to_favourites)
