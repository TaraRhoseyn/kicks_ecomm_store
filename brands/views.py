from django.shortcuts import render
from products.models import ProductBrand
import string


def show_brand(request):
    """
    Show all brands.
    """
    # Credit for sort ProductBrand.objects method: Reddit
    brands = ProductBrand.objects.all().order_by('name')    
    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)
