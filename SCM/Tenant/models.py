from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint

from SCM.Tenant.utils import get_current_tenant, get_state

UserModel = get_user_model()

# Create your models here.
class Tenant(models.Model):
    tenant = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.tenant

class TenantManager(models.Manager):
    def get_queryset(self):
        state = get_state()
        queryset = super().get_queryset()

        if not state.get("enabled", True):
            return queryset

        tenant = get_current_tenant()
        queryset = queryset.filter(tenant__id=tenant.id)
        return queryset
    
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        tenant = get_current_tenant()
        for obj in objs:
            if hasattr(obj, "tenant_id"):
                obj.tenant = tenant

        return super().bulk_create(objs, batch_size, ignore_conflicts)

class TenantAwareMixin(models.Model):
    tenant = models.ForeignKey(
        to=settings.TENANT_MODEL,
        on_delete=models.CASCADE,
        editable=False,
    )
    objects = TenantManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.tenant_id:
            self.tenant = get_current_tenant()
            print(self.tenant)

        super().save(*args, **kwargs)

class UserToTenant(TenantAwareMixin):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            UniqueConstraint(
            fields=['user','tenant'], 
            name='tenant_user_uniqueness'
            )
        ]
    def __str__(self):
        return str(self.user) + "-" + str(self.tenant)
