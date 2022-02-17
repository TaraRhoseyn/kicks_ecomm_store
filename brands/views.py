# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.shortcuts import render

# Internal:
from brands.models import Brand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def show_brand(request):
    """
    View to return all brands ordered alphabetically
    Args:
        request (object): HTTP request object
    Returns:
        Brand page with passed context object
    """
    # Credit for sort Brand.objects method: Reddit
    brands = Brand.objects.all().order_by('name')    
    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)
