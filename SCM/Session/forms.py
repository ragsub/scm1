from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from SCM.forms import CustomErrorList

class LoginForm(AuthenticationForm):
    template_name = 'scm/form_template.html'

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Enter e-mail address',
                'autofocus':'autofocus',
                'autocomplete':'username',
                'size':30
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter password',
                'autocomplete':'current-password', 
                'size':30
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList