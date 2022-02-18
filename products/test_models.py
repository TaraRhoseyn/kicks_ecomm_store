# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party:
from django.test import TestCase

# Internal:
from .models import ProductGroup, ProductType, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test Product, ProductGroup, and ProductType
        """
        ProductGroup.objects.create(
            name='test-brand', friendly_name='test brand')
        ProductType.objects.create(
            name='test-brand', friendly_name='test brand')
        Product.objects.create(
            sku='TRANICH3BL',
            name='Test Name',
            description='Test description',
            product_brand='1',
            product_group='1',
            product_type='1',
            price='99.99',
            default_rating='1',
            image = 'test.png',
            image_url='www.test.com/test.png'
        )

    def test_group_str_method(self):
        """
        Tests the ProductGroup method and verifies
        """
        group = ProductGroup.objects.get(name='test-group')
        self.assertEqual((group.__str__()), group.name)
        self.assertEqual(group.get_friendly_name(), group.friendly_name)
    
    def test_type_str_method(self):
        """
        Tests the ProductType method and verifies
        """
        product_type = ProductType.objects.get(name='test-product_type')
        self.assertEqual((product_type.__str__()), product_type.name)
        self.assertEqual(product_type.get_friendly_name(), product_type.friendly_name)

    def test_product_str_method(self):
        """
        Tests the products str method and verifies
        """
        product = Product.objects.get(pk='1')
        self.assertEqual((product.__str__()), product.name)
    
    def tearDown(self):
        """
        Delete test Product, ProductBrand, ProductGroup, and ProductType
        """
        Product.objects.all().delete()
        ProductGroup.objects.all().delete()
        ProductType.objects.all().delete()
