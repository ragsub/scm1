from urllib import response
from django.http import Http404, HttpRequest
from SCM.Tenant.utils import no_tenant_context, tenant_context
from SCM.Tenant.models import Tenant

class TenantIdentification:
    
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request:HttpRequest):
        path = request.path
        path_params = path.split('/')
        if len(path_params) > 2:
            tenant = Tenant.objects.filter(tenant = path_params[2]).first()
        else:
            tenant = None
            
        if (path_params[1] != 'shop') | (tenant == None):
            with no_tenant_context():
                response =  self.get_response(request)
        else:
            if not hasattr(request, 'tenant'):
                request.tenant = tenant.tenant
            with tenant_context(tenant):
                response = self.get_response(request)

        return response