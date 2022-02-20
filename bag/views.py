# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

# Internal:
from products.models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_shopping_bag(request):
    """
    View that renders the bag contents page
    Args:
        request (object): HTTP request object
    Returns:
        Bag page.
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add items to shopping bag with quantity and size
    Args:
        request (object): HTTP request object
        item_id: Item identifier
    Returns:
        redirect_url: Redirect to bag url
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # checks if bag var in session, creates one if not
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 f'Added size {product.name} (size {size}) '
                                 f'quantity to'
                                 f'{bag[item_id]["items_by_size"]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 f'Added size {product.name} '
                                 f'(size {size}) to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             f'Added size {product.name} '
                             f'(size {size}) to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} '
                             f'quantity to {quantity}')
        else:
            bag[item_id] = quantity
            messages.success(request,
                             f'Added {product.name} '
                             f'to your bag')

    # overwrites var with session var
    request.session['bag'] = bag
    # redirects users
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of bag items to a specified amount
    Args:
        request (object): HTTP request object
        item_id: Item identifier
    Returns:
        Redirect to bag url
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Updated {product.name} '
                             f'(size {size}) quantity '
                             f'to {quantity}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request,
                                 f'Removed size {product.name} '
                                 f'(size {size}) to your bag')

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             f'Updated {product.name} '
                             f'quantity to {quantity}')

        else:
            bag.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} '
                             f'from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    Args:
        request (object): HTTP request object
        item_id: Item identifier
    Returns:
        Http response of 200 (no error arising)
    """
    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request,
                                 f'Removed size {size} '
                                 f'{product.name} to your bag')
        else:
            bag.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} '
                             f'from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
