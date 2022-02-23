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
        'created_by',
    )
    search_fields = (
        'created_by',
    )
    list_filter = (
        'created_by',
    )


admin.site.register(Favourite, FavouriteAdmin)
