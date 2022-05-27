from django import forms
from django.core.validators import FileExtensionValidator

from SCM.Store.models import Store
from SCM.forms import CustomModelForm

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
