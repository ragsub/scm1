from cProfile import label
from tabnanny import verbose
from django.db import models
from SCM.Tenant.models import TenantAwareMixin 

# Create your models here.
class Store(TenantAwareMixin):
    code = models.CharField(max_length=20, verbose_name='Store Code')
    description = models.CharField(max_length=50, verbose_name='Store Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Store Detail')
    latitude = models.FloatField(verbose_name='Store Latitude')
    longitude = models.FloatField(verbose_name='Store Longitude')

    def __str__(self):
        return self.description
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_location_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_location_description')
        ]
        ordering = ['code']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    
        

