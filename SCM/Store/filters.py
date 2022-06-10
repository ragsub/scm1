from django_filters import FilterSet
from django_filters import CharFilter, ModelChoiceFilter, BooleanFilter
from django_filters.widgets import BooleanWidget
from django import forms

from SCM.Store.models import Store, ProductInStore
from SCM.Product.models import Product

from SCM.forms import FilterForm, SwitchWidget


class StoreFilter(FilterSet):
    code = CharFilter(label='Store Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Store Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Store Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        form = FilterForm
        model = Store
        fields = ['code','description','detail']

class ProductInStoreFilter(FilterSet):
    product = ModelChoiceFilter(label='Product', queryset=Product.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    store = ModelChoiceFilter(label='Store', queryset=Store.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    active = BooleanFilter(label='Active', widget = BooleanWidget(attrs={'class':'form-select'}))

    class Meta:
        form = FilterForm
        model = ProductInStore
        fields = ['store','product','active']

