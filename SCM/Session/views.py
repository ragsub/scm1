from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render

from SCM.Session.forms import LoginForm

from SCM.Tenant.utils import no_tenant_context, create_user_session
from SCM.Tenant.crud import get_tenants_for_user

# Create your views here.
class LoginUser(LoginView):
    template_name = 'session/login.html'
    authentication_form = LoginForm

    def get_context_data(self, **kwargs):
        logout(self.request)
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        with no_tenant_context():
            tenant_for_user = get_tenants_for_user(self.request.user)
        create_user_session(self.request, tenant_for_user.tenant)
        return super().get_success_url()

def welcome_user(request):
    context={}
    return render(request=request, template_name='session/welcome.html',context=context)