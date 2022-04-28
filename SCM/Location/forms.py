from django import forms
from django.core.validators import FileExtensionValidator

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

class UploadLocationForm(forms.Form):
    file = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv'])], label="Upload Location File", widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.description='Upload Locations'
        super (UploadLocationForm, self).__init__ (*args, **kwargs)
