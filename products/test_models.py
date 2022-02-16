# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party:
from django.test import TestCase

# Internal:
from products.models import ProductBrand, ProductGroup, ProductType, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test Product, ProductBrand, ProductGroup, and ProductType
        """
        ProductBrand.objects.create(
            name='test-brand', friendly_name='test brand')

        ProductGroup.objects.create(
            name='test-brand', friendly_name='test brand')

        ProductType.objects.create(
            name='test-brand', friendly_name='test brand')

        Product.objects.create(
            sku='TRANICH3BL',
            name='Test Name',
            description='Test description',
            product_brand=1,
            product_group=1,
            product_type=1,
            price='99.99',
            rating='1',
            image_url='test.png'
        )

    def tearDown(self):
        """
        Delete test Product, ProductBrand, ProductGroup, and ProductType
        """
        Product.objects.all().delete()
        ProductBrand.objects.all().delete()
        ProductGroup.objects.all().delete()
        ProductType.objects.all().delete()

    def test_brand_str_method(self):
        """
        This test tests the ProductBrand method and verifies
        """
        brand = ProductBrand.objects.get(name='test-brand')
        self.assertEqual((brand.__str__()), brand.name)
        self.assertEqual(brand.get_friendly_name(), brand.friendly_name)

    def test_product_str_method(self):
        """
        This test tests the products str method and verifies
        """
        product = Product.objects.get(pk='1')
        self.assertEqual((product.__str__()), product.name) 