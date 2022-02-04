from django.contrib import admin
from .models import Product, ProductGroup, ProductType, ProductBrand


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


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)