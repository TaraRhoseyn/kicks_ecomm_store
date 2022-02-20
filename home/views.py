# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def index(request):
    """
    A view to return the home page
    Args:
        request (object): HTTP request object
    Returns:
        Home page
    """
    return render(request, 'home/index.html')
