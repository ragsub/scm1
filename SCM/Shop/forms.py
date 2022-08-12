from django import forms

from SCM.Shop.models import Cart
from SCM.forms import EditModelForm

class AddCartForm(EditModelForm):
    
    class Meta:
        model = Cart
        fields = ['product','price','quantity','total_price']

        widgets = {
            'product': forms.HiddenInput(attrs={'class': 'form-select','readonly':'readonly'}),
            'price': forms.HiddenInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'total_price': forms.HiddenInput(attrs={'class': 'form-control','readonly':'readonly'}),
        }