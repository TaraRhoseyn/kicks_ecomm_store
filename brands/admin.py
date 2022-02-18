# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.contrib import admin

# Internal
from brands.models import Brand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )

admin.site.register(Brand, BrandAdmin)
