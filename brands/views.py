# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, reverse, redirect

# Internal
from .models import Brand
from .forms import BrandForm

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

@login_required
def add_brand(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added brand!')
            return redirect(reverse('individual_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add brand. Please ensure the form is valid.')
    else:
        form = BrandForm()

    template = 'brands/add_brand.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

