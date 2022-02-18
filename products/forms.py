# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS 

# Third party
from django import forms

# Internal
from .models import Review, Product, ProductGroup, ProductType
from brands.models import Brand
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RatingForm(forms.ModelForm):
    class Meta:
        exclude = ('user', 'product', 'created_by', 'created_at')
        model = Review
        fields = '__all__'
        labels = {
            'star_rating': 'Select your rating',
            'text_review': 'Write your review'
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product_groups = ProductGroup.objects.all()
        friendly_names = [
            (g.id, g.get_friendly_name()) for g in product_groups]
        product_types = ProductType.objects.all()
        friendly_names = [
            (t.id, t.get_friendly_name()) for t in product_types]
        brands = Brand.objects.all()
        friendly_names = [
            (b.id, b.get_friendly_name()) for b in brands]

        self.fields['product_groups'].choices = friendly_names
        self.fields['product_types'].choices = friendly_names
        self.fields['brands'].choices = friendly_names
