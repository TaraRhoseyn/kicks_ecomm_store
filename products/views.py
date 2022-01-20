from django.shortcuts import render
from .models import Product, ProductGroup, ProductType

def show_all_products(request):
    """
    Show all products.
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
