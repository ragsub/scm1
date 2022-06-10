from django.db import models
from SCM.Tenant.models import TenantAwareMixin 
from SCM.Product.models import Product

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
            models.UniqueConstraint(fields=['tenant','code'], name='unique_store_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_store_description')
        ]
        ordering = ['code']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class ProductInStore(TenantAwareMixin):
    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.PROTECT)
    store = models.ForeignKey(to=Store, verbose_name='Store', on_delete=models.PROTECT)
    list_price = models.FloatField(verbose_name = 'Product List Price') 
    discounted_price = models.FloatField(verbose_name='Product Discounted Price')
    active = models.BooleanField(verbose_name='Product Active',choices=((True,'Active'),(False,'Inactive')))

    def __str__(self):
        return str(self.store) + ' ' + str(self.product)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','product','store'], name='unique_store_product'),
        ]
        ordering = ['store','product']
        verbose_name = 'Product in Store'
        verbose_name_plural = 'Products in Store'

        

