from SCM.Tenant.models import UserToTenant, Tenant
from SCM.Tenant.exceptions import TenantNotFoundError

def add_user_to_tenant(user, tenant):
    new_user_to_tenant = UserToTenant(
        user=user, 
        tenant=tenant
    )
    new_user_to_tenant.save()

def get_tenants_for_user(user):
    tenants_for_user = UserToTenant.objects.filter(user=user).first()
    if not tenants_for_user:
        raise TenantNotFoundError("No Tenant mapped for User")
    return tenants_for_user

def get_tenant_from_id(tenant_id):
    return Tenant.objects.get(pk=tenant_id)