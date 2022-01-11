from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=12, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField()
    product_group = models.ForeignKey('ProductGroup', null=True, blank=True)
    product_type = models.ForeignKey('ProductType', null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False)
    rating = models.IntegerField(max_digitals=1, null=False, blank=False)
    brand = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
