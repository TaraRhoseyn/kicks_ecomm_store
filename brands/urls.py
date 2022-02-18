from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_brand, name='brands'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit_brand/<brand_name>/', views.edit_brand, 
        name='edit_brand'),
]
