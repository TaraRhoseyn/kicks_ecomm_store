# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.contrib import admin

# Internal
from .models import Product, ProductGroup, ProductType, Review

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'product_group',
        'product_type',
        'price',
        'default_rating',
        'product_brand',
        'image_url',
        'image',
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




class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text_review',
        'star_rating',
        'created_by',
        'product',
        'created_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Review, ReviewAdmin)