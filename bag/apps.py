# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party:
from django.apps import AppConfig


class ShoppingbagConfig(AppConfig):
    """
    A class for configuring a bag
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
