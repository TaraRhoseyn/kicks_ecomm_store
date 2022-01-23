from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_products, name='products'),
    path('<product_id>', views.show_individual_product, name='individual_product')
]
