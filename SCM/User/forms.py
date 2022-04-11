from django import forms
from django.contrib.auth.forms import UserCreationForm

from SCM.User.models import User

from SCM.forms import CustomErrorList

class NewUserForm(UserCreationForm):
    template_name = 'scm/form_template.html'

    def __init__(self, *args, **kwargs) -> None:
        kwargs_new = {'error_class': CustomErrorList}
        kwargs_new.update(kwargs)
        super().__init__(*args, **kwargs_new)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
                'class':'form-control w-100',
                'autocomplete':'off'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirm',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class':'form-control',
                'autocomplete':'off'
            }
        )    
    )    
    
    class Meta:
        model = User
        fields = ('email','password1','password2')
        labels = {
            'email':'Email'
        }
        widgets = {
            'email':forms.TextInput(
                attrs={
                    'placeholder':'Enter email',
                    'class':'form-control',
                    'size':'2',
                    'autocomplete':'on'
                }
            )
        }