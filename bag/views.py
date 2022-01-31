from django.shortcuts import render

def view_shopping_bag(request):
    """ A view to render shopping bag page """
    return render(request, 'bag/bag.html')
