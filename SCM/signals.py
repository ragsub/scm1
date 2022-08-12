from django.contrib.auth.models import Group, Permission

def add_tenant_authorization(instance, ct):
    tenant = instance.tenant
    tenant_group, created = Group.objects.get_or_create(name=tenant)
    access, created = Permission.objects.get_or_create(codename=tenant,name='Can access '+str(tenant),content_type=ct)
    tenant_group.permissions.add(access)        