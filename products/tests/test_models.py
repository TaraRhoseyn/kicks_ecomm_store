from django.test import TestCase
from products.models import Product, ProductGroup, ProductType

class TestStrReturns(TestCase):
    """
    Test that the Product models return strings
    Credit to test-driven-django-development
    for model testing functions
    """

    def test_str_product_name(self):
        strProductName = Product(name="Nike trainers")
        self.assertEqual(str(strProductName), strProductName.name)
    
    def test_str_product_group_name(self):
        strGroupName = ProductGroup(name="mens")
        self.assertEqual(str(strGroupName), strGroupName.name)
    
    def test_str_product_type_name(self):
        strTypeName = ProductType(name="sandals")
        self.assertEqual(str(strTypeName), strTypeName.name)
