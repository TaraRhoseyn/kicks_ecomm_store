# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase

# Internal
from .forms import OrderForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestOrderForm(TestCase):
    """
    Tests ordering form
    """
    def test_add_order_form(self):
        """
        Tests the order form object
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@email.com',
            'phone_number': '123456',
            'country': 'GB',
            'town_or_city': 'test city',
            'street_address1': 'test address 1',
            'street_address2': 'test address 2',
            })
        self.assertTrue(form.is_valid())
