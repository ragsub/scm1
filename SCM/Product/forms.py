from unicodedata import category
from django import forms

from SCM.forms import CustomModelForm
from SCM.Product.models import Category, Product

class AddCategoryForm(CustomModelForm):
    class Meta:
        model = Category
        fields = ['code','description','detail']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'code': 'Category Code:',
            'description':'Category Description:',
            'detail':'Category Detail:',
        }

class AddProductForm(CustomModelForm):
    class Meta:
        model = Product
        fields = ['category','code','description','detail','photo']
        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'category':'Product Category',
            'code': 'Product Code:',
            'description':'Product Description:',
            'detail':'Product Detail:',
            'photo':'Product Photo'
        }