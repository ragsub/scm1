from django import forms
from django_filters import FilterSet, CharFilter, ModelChoiceFilter


from SCM.forms import FilterForm
from SCM.Product.models import Category, Product

class CategoryFilter(FilterSet):
    code = CharFilter(label='Category Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Category Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Category Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        form = FilterForm
        model = Category
        fields = ['code','description','detail']

class ProductFilter(FilterSet):
    category = ModelChoiceFilter(label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    code = CharFilter(label='Category Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Category Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Category Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        form = FilterForm
        model = Product
        fields = ['category','code','description','detail']


