from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from allauth.account.views import PasswordChangeView


# Create your views here.
def welcome_user(request, tenant_name):
    context={}
    context['tenant_name'] = tenant_name
    return render(request=request, template_name='session/welcome.html',context=context)

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    pass
