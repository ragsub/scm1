from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "shop/{tenant}/account/welcome/"
        return path.format(tenant=request.tenant.tenant)