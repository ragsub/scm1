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

class EditModelForm(forms.ModelForm):
    template_name = 'scm/edit_form_template.html'    
    def __init__(self, *args, **kwargs):
        super(EditModelForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList


class FilterForm(forms.Form):
    template_name = 'scm/filter_form_template.html'

class DataListWidget(forms.widgets.Select):
    template_name='scm/datalist.html'
    option_template_name = 'scm/datalist_option.html'

class SwitchWidget(forms.widgets.CheckboxInput):
    template_name='scm/switch.html'

