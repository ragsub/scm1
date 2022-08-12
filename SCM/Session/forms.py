from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class LoginForm(AuthenticationForm):

    username = UsernameField()
    password = forms.CharField(widget=forms.PasswordInput())