from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # sku = models.CharField(max_length=254, null=True, blank=True)
    # friendly_name = models.CharField(max_length=254)
    # description = models .TextField()
    # # TODO add status field here.
    # is_clearance = models.BooleanField(default=False, null=True, blank=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)
    # product_gender = models.ForeignKey('ProductGender', null=False,blank=False)
    # product_type = models.ForeignKey('ProductType', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# class ProductType(models.Model):
#     product_type = models.CharField(max_length=15, null=False, blank=False)


# class ProductGroup(models.Model):
#     product_group = models.CharField(max_length=15, null=False, blank=False)
