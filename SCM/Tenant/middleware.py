from SCM.Tenant.utils import no_tenant_context, tenant_context, get_tenant_from_session

class TenantIdentification(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        if request.user.is_authenticated:
            user = request.user
            
            tenant = get_tenant_from_session(request)

            with tenant_context(tenant):
                response = self.get_response(request)
        else:
            response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response