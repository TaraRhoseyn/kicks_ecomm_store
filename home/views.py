from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view to return the home page
    Args:
        request (object): HTTP request object
    Returns:
        Home page
    """
    return render(request, 'home/index.html')
