# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.apps import AppConfig

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FavouritesConfig(AppConfig):
    """
    App configuration setup for favourites app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favourites'
