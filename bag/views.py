from django.shortcuts import render, redirect

def view_shopping_bag(request):
    """ A view to render shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add items to shopping bag """
    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # checks if bag var in session, creates one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += qty
    else:
        bag[item_id] = qty
    
    # overwrites var with session var
    request.session['bag'] = bag
    # redirects users
    return redirect(redirect_url)
