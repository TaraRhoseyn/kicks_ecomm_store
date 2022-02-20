# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase
from django.contrib.auth.models import User

# Internal
from products.models import Product
from .models import Favourite

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestFavouriteModels(TestCase):
    """
    A class for testing Favourite models
    """
    def setUp(self):
        """
        Create a test product, user and favourites
        """
        user = User.objects.create_user(
            username='test_user', 
            password='test_password'
        )
        Product.objects.create(
            name='test_name',
            price='99.99',
            description='test_description',
            default_rating='2',
        )
        Favourite.objects.create(
            created_by=user
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
        favourite = Favourite.objects.get()
        self.assertEqual(str(favourite.__str__()), favourite.__str__())
