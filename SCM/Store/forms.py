from django import forms

from SCM.Store.models import Store, ProductInStore
from SCM.forms import CustomModelForm, SwitchWidget, EditModelForm

class AddStoreForm(CustomModelForm):
    class Meta:
        model = Store
        fields = ['code','description','detail','latitude','longitude']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'code': 'Store Code:',
            'description':'Store Description:',
            'detail':'Store Detail:',
            'latitude':'Store Latitude',
            'longitude':'Store Longitude'
        }

class AddProductInStoreForm(EditModelForm):
    class Meta:
        model = ProductInStore
        fields = ['store','product','list_price','discounted_price','active']
        widgets = {
            'store': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'list_price': forms.TextInput(attrs={'class': 'form-control'}),
            'discounted_price': forms.TextInput(attrs={'class': 'form-control'}),
            'active': SwitchWidget(attrs={'class': 'form-check-input'})
        }
