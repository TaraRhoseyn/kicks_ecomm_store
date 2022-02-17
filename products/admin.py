# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.contrib import admin

# Internal
from brands.models import Brand
from .models import Product, ProductGroup, ProductType

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'product_group',
        'product_type',
        'price',
        'rating',
        'product_brand',
        'image_url',
        'has_sizes'
    )

    ordering = ('sku',)


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Brand, BrandAdmin)