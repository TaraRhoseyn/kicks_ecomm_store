import requests
from django import forms
from .models import Review

class RatingForm(forms.ModelForm):
    class Meta:
        exclude = ('user', 'product', 'created_by' 'created_at')
        model = Review
        fields = '__all__'
        labels = {
            'star_rating': 'Select your rating',
            'text_review': 'Write your review'
        }