from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from SCM.Tenant.utils import no_tenant_context, create_user_session
from SCM.Tenant.crud import get_tenants_for_user


class LoginUser(LoginView):
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        logout(self.request)
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        with no_tenant_context():
            tenant_for_user = get_tenants_for_user(self.request.user)
        create_user_session(self.request.user, tenant_for_user.tenant)
        return super().get_success_url()



