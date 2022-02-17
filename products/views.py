# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from django.db.models.functions import Lower

# Internal:
from .models import Product, ProductGroup, ProductType
from brands.models import Brand
from favourites.models import Favourite

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def show_all_products(request):
    """
    View to returns all products, sort products 
    by object keys and search queries
    Args:
        request (object): HTTP request object
    Returns:
        Products page(s) with passed context object
    """

    search = None
    product_groups = None
    product_types = None
    product_brands = None
    sort = None
    direction = None
    products = Product.objects.all()
    

    if request.GET:

        # Sorting products by type 
        if 'product_type' in request.GET:
            product_types = request.GET['product_type'].split(',')
            products = products.filter(product_type__name__in=product_types)
            product_types = ProductType.objects.filter(name__in=product_types)

        # Sorting products by group
        if 'product_group' in request.GET:
            product_groups = request.GET['product_group'].split(',')
            products = products.filter(product_group__name__in=product_groups)
            product_groups = ProductGroup.objects.filter(name__in=product_groups)

        if 'product_brand' in request.GET:
            product_brands = request.GET['product_brand'].split(',')
            products = products.filter(product_brand__name__in=product_brands)
            product_brands = Brand.objects.filter(name__in=product_brands)

        # User searching products
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                # If search bar is blank:
                messages.error(request, "Please fill out the search bar.")
                return redirect(reverse('products'))
            searches = Q(name__icontains=search) | Q(description__icontains=search)
            products = products.filter(searches)
       
       # User sorting products
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'product_group': product_groups,
        'product_type': product_types,
        'product_brand': product_brands,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def show_individual_product(request, product_id):
    """
    View to returns all products, sort products 
    by object keys and search queries
    Args:
        request (object): HTTP request object
        product_id key value of Product model
    Returns:
        Individual product page(s) with passed context object
    """

    product = get_object_or_404(Product, pk=product_id)

    # Grabs favourites
    try:
        favourites = get_object_or_404(Favourite, created_by=request.user.id)
    except Http404:
        is_product_in_favourites = False
    else:
        is_product_in_favourites = bool(product in favourites.products.all())

    context = {
        'product': product,
        'is_product_in_favourites': is_product_in_favourites,
    }

    return render(request, 'products/individual_product.html', context)
