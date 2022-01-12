from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
    # def setUp(self):
    #     product = Product.objects.create(name='Product1')

    """
    Credit to test-driven-django-development
    for model testing functions
    """
    # Test text fields
    def test_string_representation(self):
        stringName = Product(name="Nike trainers")
        self.assertEqual(str(stringName), stringName.name)