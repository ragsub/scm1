from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser):
    username = models.CharField(max_length=50,default="")
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS

    objects = UserManager()