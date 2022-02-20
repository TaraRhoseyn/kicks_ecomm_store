# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.db import models
from django.contrib.auth.models import User

# Internal
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Favourite(models.Model):
    """
    Holds products favourited by users.
    """
    class Meta:
        verbose_name_plural = 'Favourites'

    products = models.ManyToManyField(
        Product,
        blank=True
    )
    created_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Return object string
        Args:
            self (object): self object.
        Returns:
            str: users favourite string
        """
        return f"Your Favourites"
