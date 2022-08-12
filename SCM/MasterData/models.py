from django.db import models

from SCM.models import GrantTenantPermissionMixin
from SCM.Tenant.models import TenantAwareMixin 

# Create your models here.
class Store(GrantTenantPermissionMixin, TenantAwareMixin):
    code = models.CharField(max_length=20, verbose_name='Store Code')
    description = models.CharField(max_length=50, verbose_name='Store Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Store Detail')
    latitude = models.FloatField(verbose_name='Store Latitude')
    longitude = models.FloatField(verbose_name='Store Longitude')

    def __str__(self):
        return self.description
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_store_code',),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_store_description')
        ]
        ordering = ['code']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class Category(GrantTenantPermissionMixin, TenantAwareMixin):
    code = models.CharField(max_length=20, verbose_name='Store Code')
    description = models.CharField(max_length=50, verbose_name='Store Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Store Detail')
    
    def __str__(self):
        return self.description
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_category_code',),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_category_description')
        ]
        ordering = ['code']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
