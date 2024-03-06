from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'pname': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),  # Corrected typo here
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'image1': forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
        }