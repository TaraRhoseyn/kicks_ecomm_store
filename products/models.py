from django.db import models
from django.core.validators import MaxValueValidator


class ProductGroup(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductType(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductBrand(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=12, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField()
    product_group = models.ForeignKey(
        'ProductGroup', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(
        'ProductType', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False)
    rating = models.IntegerField(
        null=False, blank=False, validators=[MaxValueValidator(999)])
    product_brand = models.ForeignKey(
        'ProductBrand', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.CharField(
        max_length=40, null=False, blank=False, default='SOME STRING')
    has_sizes = models.BooleanField(
        default=True, null=False, blank=False)

    def __str__(self):
        return self.name
