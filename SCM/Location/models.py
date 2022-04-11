from django.db import models
from SCM.Tenant.models import TenantAwareMixin 

# Create your models here.
class Location(TenantAwareMixin):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    detail = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_location_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_location_description')
        ]
        ordering = ['code']
