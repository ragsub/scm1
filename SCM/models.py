from django.contrib.auth.models import Group

from guardian.shortcuts import assign_perm

class GrantTenantPermissionMixin:
    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)
        tenant_group = Group.objects.get(name=self.tenant)        
        assign_perm(str(self.tenant),tenant_group,self)
        return obj


