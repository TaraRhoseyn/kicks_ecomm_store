# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase

# Internal
from products.models import Product
from .models import Favourite
from profiles.models import User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestFavouriteModels(TestCase):
    """
    A class for testing Favourite models
    """
    def setUp(self):
        """
        Create a test product, user and favourites
        """
        Product.objects.create(
            name='Test Name',
            price='99.99',
            description='Test Description',
        )
        User.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address',
        )
        Favourite.objects.create(
            products='Test Name',
            created_by='testname'
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Product.objects.all().delete()
        User.objects.all().delete()
        Favourite.objects.all().delete()

    def test_fav_str_method(self):
        """
        Tests string return of Favourite model
        """
        favourite = Favourite.objects.get(created_by='testname')
        self.assertEqual(str(favourite), favourite.created_by)
