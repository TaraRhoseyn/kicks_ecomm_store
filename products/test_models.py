# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase

# Internal
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
            name='testgroup',
            friendly_name='test_group')
        ProductType.objects.create(
            name='testtype',
            friendly_name='test type')
        Product.objects.create(
            sku='TRANICH3BL',
            name='testname',
            description='Test description',
            price='99.99',
            default_rating='1',
            image = 'test.png',
            image_url='www.test.com/test.png'
        )
    
    def tearDown(self):
        """
        Delete test Product, ProductGroup, and ProductType
        """
        Product.objects.all().delete()
        ProductGroup.objects.all().delete()
        ProductType.objects.all().delete()

    def test_group_str_method(self):
        """
        Tests the ProductGroup method and verifies
        """
        group = ProductGroup.objects.get(name='testgroup')
        self.assertEqual((group.__str__()), group.name)
    
    def test_type_str_method(self):
        """
        Tests the ProductType method and verifies
        """
        product_type = ProductType.objects.get(name='testtype')
        self.assertEqual((product_type.__str__()), product_type.name)

    def test_product_str_method(self):
        """
        Tests the products str method and verifies
        """
        product = Product.objects.get(name='testname')
        self.assertEqual((product.__str__()), product.name)

