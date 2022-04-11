from django_filters import FilterSet
from django_filters import CharFilter
from django import forms

from SCM.Location.models import Location

class FilterForm(forms.Form):
    template_name = 'scm/filter_form_template.html'


class LocationFilter(FilterSet):
    code = CharFilter(label='Code:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    description = CharFilter(label='Description:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))
    detail = CharFilter(label='Detail:', lookup_expr='icontains', widget = forms.TextInput(attrs={'class':'form-control','size':'10'}))

    class Meta:
        form = FilterForm
        model = Location
        fields = ['code','description','detail']

