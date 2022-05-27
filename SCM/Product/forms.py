from django import forms
from string import Template
from django.utils.safestring import mark_safe

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

class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs, **kwargs)
        if hasattr(value, 'url'):
            print ('value is')
            print(value.url)
            img_html = mark_safe(
                f'<br><img src="{value.url}" width="200" />')
            return f'{input_html}{img_html}'
        return input_html


class AddProductForm(CustomModelForm):
    photo = forms.ImageField(widget=ImagePreviewWidget(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['category','code','description','detail','photo']
        widgets = {
            'category':forms.Select(attrs={'class':'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'category':'Product Category',
            'code': 'Product Code:',
            'description':'Product Description:',
            'detail':'Product Detail:',
            'photo':'Product Photo'
        }