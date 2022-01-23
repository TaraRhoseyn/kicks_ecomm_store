from django.shortcuts import get_object_or_404, render
from .models import Product, ProductGroup, ProductType


def show_all_products(request):
    """
    Returns all products.
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def show_individual_product(request, product_id):
    """
    Returns individual product details.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/individual_product.html', context)
