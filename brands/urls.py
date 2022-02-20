# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.urls import path

# Internal
from . import views

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.show_brand, name='brands'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit_brand/<brand_name>/', views.edit_brand,
         name='edit_brand'),
    path('delete_brand/<brand_name>/', views.delete_brand,
         name='delete_brand'),
]
