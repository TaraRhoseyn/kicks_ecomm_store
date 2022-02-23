# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.contrib import admin

# Internal
from .models import Favourite
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FavouriteAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = (
        'products',
        'created_by',
    )
    search_fields = (
        'products',
        'created_by',
    )
    list_filter = (
        'products',
        'created_by',
    )


admin.site.register(Favourite, FavouriteAdmin)
