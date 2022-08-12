from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.functions import Cast
from django.db.models.expressions import BaseExpression
from django.db.models.constraints import UniqueConstraint

from SCM.Tenant.utils import get_current_tenant, get_state

UserModel = get_user_model()

# Create your models here.

class CurrentTenant(BaseExpression):
    def as_sql(self, compiler, connection, *args, **kwargs):
        current_tenant = get_current_tenant()
        tenant_id = str(current_tenant.id)
        value = self.output_field.get_db_prep_value(tenant_id, connection)
        return "%s", [str(value)]

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

        field = self.model.tenant.field.target_field
        cr = CurrentTenant(output_field=field)

        queryset = queryset.filter(tenant_id=Cast(cr, output_field=field))

        # tenant = get_current_tenant()
        # queryset = queryset.filter(tenant__id=tenant.id)
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

   

