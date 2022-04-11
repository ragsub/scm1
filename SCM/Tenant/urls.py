from django.urls import path
from django.contrib.auth.views import LoginView

from SCM.Tenant.views import register_tenant

app_name = 'SCM.Tenant'

urlpatterns=[
    path('register/', register_tenant, name='register'),
]