from cProfile import label
from tabnanny import verbose
from django.db import models
from SCM.Tenant.models import TenantAwareMixin 

# Create your models here.
class Location(TenantAwareMixin):
    code = models.CharField(max_length=20, verbose_name='Location Code')
    description = models.CharField(max_length=50, verbose_name='Location Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Location Detail')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_location_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_location_description')
        ]
        ordering = ['code']
