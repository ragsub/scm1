from django import forms
from django.contrib.auth.forms import UserCreationForm

from SCM.User.models import User

from SCM.forms import CustomErrorList

class NewUserForm(UserCreationForm):


    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm')
    
    class Meta:
        model = User
        fields = ('email','password1')