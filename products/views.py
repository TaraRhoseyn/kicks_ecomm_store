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
from .forms import RatingForm, ProductForm
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
    View to returns individual product view 
    with favourites and reviews if available.
    Args:
        request (object): HTTP request object
        product_id key value of Product model
    Returns:
        Individual product page(s) with passed context object
    """

    product = get_object_or_404(Product, pk=product_id)
    

    # Retrieves favourites if favourite matches user and product
    try:
        favourites = get_object_or_404(Favourite, created_by=request.user.id)
    except Http404:
        is_product_in_favourites = False
    else:
        is_product_in_favourites = bool(product in favourites.products.all())
    
    # Retrieves reviews if review matches product
    if Review.objects.filter(product__id__exact=product_id):
        reviews = Review.objects.filter(product__id__exact=product_id)
        context = {
            'product': product,
            'is_product_in_favourites': is_product_in_favourites,
            'reviews': reviews,
        }
    else:
        context = {
            'product': product,
            'is_product_in_favourites': is_product_in_favourites,
        }

    return render(request, 'products/individual_product.html', context)


@login_required
def add_review(request, product_id):
    """
    Add product reviews on individual products.
    Args:
        request (object): HTTP request object
        product_id key value of Product model
    Returns:
        Individual product page(s) with passed context object
    """
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


@login_required
def edit_review(request, review_id):
    """
    Edit product reviews on individual products.
    Args:
        request (object): HTTP request object
        review_id key value of Review model
    Returns:
        Individual product page(s) with passed context object
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser or request.user == review.created_by:
        if request.method == 'POST':
            review_form = RatingForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.info(request, 'Your review has been updated!')
                return redirect(reverse('individual_product',
                                args=[review.product.id]))
            else:
                messages.error(request, 'Failed to update the review. \
                                        Please ensure the form is valid.')
        else:
            review_form = RatingForm(instance=review)
    else:
        messages.error(
            request, 'Only the reviewer can edit this review')
        return redirect(reverse('individual_product', args=[review.product.id]))
    template = 'products/edit_review.html',
    context = {
        'form': review_form,
        'review': review,
        'product_id': review.product.id
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Deletes product reviews on individual products.
    Args:
        request (object): HTTP request object
        review_id key value of Review model
    Returns:
        All products page
    """

    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser or request.user == review.created_by:
        review.delete()
        messages.info(request, 'Your review has been deleted.')
        return redirect(reverse('products'))
    else:
        messages.error(request, 'Only the reviewer can do that.')
        return redirect(reverse('products'))



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
