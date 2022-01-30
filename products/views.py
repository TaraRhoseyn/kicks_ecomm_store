from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductGroup, ProductType


def show_all_products(request):
    """
    Returns all products.
    """

    search = None
    product_groups = None
    product_types = None
    sort = None
    direction = None
    brands = None
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

        # User searching products
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                # If search bar is blank:
                messages.error(request, "Please fill out the search bar.")
                return redirect(reverse('products'))
            searches = Q(name__icontains=search) | Q(brand__icontains=search) | Q(description__icontains=search)
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
            if 'brands' in request.GET:
                brands = request.GET['brands']
            products = products.order_by(sortkey)


    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'product_group': product_groups,
        'current_sorting': current_sorting,
        'brands': brands,
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
