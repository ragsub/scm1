from django.forms.utils import ErrorList
from django import forms

class CustomErrorList(ErrorList):
    template_name = 'scm/error_template.html'

class CustomForm(forms.Form):
    template_name = 'scm/form_template.html'

    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

class CustomModelForm(forms.ModelForm):
    template_name = 'scm/form_template.html'
    def __init__(self, *args, **kwargs):
        super(CustomModelForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

class FilterForm(forms.Form):
    template_name = 'scm/filter_form_template.html'

