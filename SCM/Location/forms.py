from django import forms

from SCM.Location.models import Location

class AddLocationForm(forms.ModelForm):
    template_name = 'scm/form_template.html'
    class Meta:
        model = Location
        fields = ['code','description','detail']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'code': 'Code:',
            'description':'Description:',
            'detail':'Detail:'
        }