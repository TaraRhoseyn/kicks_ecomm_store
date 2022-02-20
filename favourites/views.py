# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Internal
from products.models import Product
from .models import Favourite
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Credit: Paul Meeneghan


@login_required
def view_favourites(request):
    """
    A view that displays users favourites
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the request, template and context
    """
    favourites_count = 0
    try:
        favourites = Favourite.objects.filter(created_by=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = favourites.products.all()
        favourites_count = favourites.products.all().count()

    template = 'favourites/favourites.html'
    context = {
        'favourites_items': favourites_items,
        'favourites_count': favourites_count
    }
    return render(request, template, context)


@login_required
def add_product_to_favourites(request, item_id):
    """
    Add a product item to favourites
    Args:
        request (object): HTTP request object.
        item_id: Item id
    Returns:
        Renders the product detail page
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourite, created_by=request.user.id)
    except Http404:
        favourites = Favourite.objects.create(created_by=request.user)
    if product in favourites.products.all():
        messages.info(request, 'Product is in favourites.')
    else:
        favourites.products.add(product)
        messages.info(request, 'Added the product to your favourites')
    return redirect(reverse('individual_product', args=[item_id]))


@login_required
def remove_product_from_favourites(request, item_id, redirect_from):
    """
    Remove a product item from favourites
    Args:
        request (object): HTTP request object.
        item_id: Item id
        redirect_from: Redirect form
    Returns:
        Reuturns the redirect url
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourite, created_by=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'Removed the product in favourites.')
    else:
        messages.error(request, 'That product is not in favourites.')
    if redirect_from == 'favourites':
        redirect_url = reverse('view_favourites')
    else:
        redirect_url = reverse('individual_product', args=[item_id])
    return redirect(redirect_url)
