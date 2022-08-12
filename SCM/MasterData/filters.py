from django_filters import FilterSet
from django_filters import CharFilter
from django import forms

from SCM.MasterData.models import Store, Category

class StoreFilter(FilterSet):
    code = CharFilter(label='Store Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Store Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Store Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        model = Store
        fields = ['code','description','detail']


class CategoryFilter(FilterSet):
    code = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    detail = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['code','description','detail']