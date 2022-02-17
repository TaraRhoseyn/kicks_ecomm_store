from django.db import models

class Brand(models.Model):
    """
    A class for brands of products, 
    e.g. Nike, Puma etc
    """
    name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )
    friendly_name = models.CharField(
        max_length=200, 
        null=True, 
        blank=True
    )

    def __str__(self):
        """
        Returns the ProductBrand name string
        Args:
            self (object): self.
        Returns:
            The ProductBrand name string
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the ProductBrand friendly name string
        Args:
            self (object): self.
        Returns:
            The ProductBrand friendly name string
        """
        return self.friendly_name
