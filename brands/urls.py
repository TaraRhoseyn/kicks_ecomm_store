from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_brand, name='brands'),
    path('add_brand/', views.add_brand, name='add_brand'),
]
