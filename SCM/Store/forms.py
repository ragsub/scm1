from django import forms
from django.core.validators import FileExtensionValidator

from SCM.Store.models import Store
from SCM.forms import CustomModelForm
class AddLocationForm(CustomModelForm):
    template_name = 'scm/form_template.html'
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
            'code': 'Code:',
            'description':'Description:',
            'detail':'Detail:',
            'latitude':'Latitude',
            'longitude':'Longitude'
        }

class UploadLocationForm(forms.Form):
    file = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv'])], label="Upload Location File", widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.description='Upload Locations'
        super (UploadLocationForm, self).__init__ (*args, **kwargs)
