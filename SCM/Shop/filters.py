from django_filters import FilterSet
from django_filters import ModelMultipleChoiceFilter, CharFilter
from django import forms


from SCM.forms import FilterForm, DataListWidget
from SCM.Store.models import ProductInStore

class ProductInStoreFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        #active_products_in_shop = kwargs.pop('active_products_in_shop')
        active_categories_in_shop = kwargs.pop('active_categories_in_shop')
        super(ProductInStoreFilter,self).__init__(*args, **kwargs)
        self.filters['category'].queryset = active_categories_in_shop
        #self.filters['product'].queryset = active_products_in_shop
    
    product = CharFilter(label='Product', field_name='product__description', lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    category = ModelMultipleChoiceFilter(label='Category', field_name='product__category_id', widget=forms.SelectMultiple(attrs={'class':'form-select','multiple':'multiple'}))

    class Meta:
        form = FilterForm
        model = ProductInStore
        fields = ['product','category']