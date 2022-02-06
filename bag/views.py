from django.shortcuts import render, redirect

def view_shopping_bag(request):
    """ A view to render shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add items to shopping bag """
    # product = get_object_or_404(Product, pk=item_id)
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
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
    
    # overwrites var with session var
    request.session['bag'] = bag
    # redirects users
    return redirect(redirect_url)
