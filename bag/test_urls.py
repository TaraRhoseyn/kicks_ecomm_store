# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Internal
from .views import view_shopping_bag, remove_from_bag, add_to_bag, adjust_bag
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBagUrls(SimpleTestCase):
    """
    Tests bag urls are resolved
    to the bag views.
    """
    def test_bag_url_resolves(self):
        url = reverse('view_shopping_bag')
        self.assertEqual(resolve(url).func, view_shopping_bag)

    def test_add_to_bag_url_resolves(self):
        url = reverse('add_to_bag', args=[1])
        self.assertEqual(resolve(url).func, add_to_bag)

    def test_adjust_bag_url_resolves(self):
        url = reverse('adjust_bag', args=[1])
        self.assertEqual(resolve(url).func, adjust_bag)

    def test_remove_from_bag_url_resolves(self):
        url = reverse('remove_from_bag', args=[1])
        self.assertEqual(resolve(url).func, remove_from_bag)
