from django import forms

from SCM.Tenant.models import Tenant

class NewTenantForm(forms.ModelForm):
    # template_name = 'scm/form_template.html'

    class Meta:
        model = Tenant
        fields = ['tenant']
        widgets = {
            'tenant': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter a unique code for your company',
                    'autocomplete':'on'})
        }
        labels = {'tenant':'Code'}



