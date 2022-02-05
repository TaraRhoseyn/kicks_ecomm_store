from django.shortcuts import render
from products.models import ProductBrand

def show_brand(request):
    """
    Show all brands.
    """

    brands = ProductBrand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)