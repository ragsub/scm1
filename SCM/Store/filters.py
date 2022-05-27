from django_filters import FilterSet
from django_filters import CharFilter
from django import forms

from SCM.Store.models import Store

from SCM.forms import FilterForm


class StoreFilter(FilterSet):
    code = CharFilter(label='Store Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Store Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Store Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        form = FilterForm
        model = Store
        fields = ['code','description','detail']

