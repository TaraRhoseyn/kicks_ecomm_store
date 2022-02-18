# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.contrib.auth.models import User

# Internal:
from .models import Product, ProductGroup, ProductType, Review
from brands.models import Brand
from favourites.models import Favourite
from .forms import RatingForm
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


@login_required
def add_review(request, product_id):
    """ Add a product review """
    product = get_object_or_404(Product, pk=product_id)
    created_by = User.objects.get(username=request.user)

    user_review = Review.objects.filter(product=product, created_by=created_by)
    review_form = RatingForm(request.POST)

    if request.method == 'POST':
        if user_review:
            messages.error(request, "You have reviewed this product already.")
            return redirect(reverse('individual_product', args=[product_id]))

        else:
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.created_by = created_by
                review.product = product
                review.save()
                messages.info(request, 'Thank you for your review!')
                return redirect(reverse('individual_product', args=[product_id]))
            else:
                messages.error(request, "Ensure the form is valid. \
                                    Please try again!")

    else:
        review_form = RatingForm(instance=product)

    template = 'products/add_review.html'
    context = {
        'form': review_form,
        'product': product,
    }

    return render(request, template, context)