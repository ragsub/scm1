from django.db import models
from pkg_resources import to_filename

from SCM.Tenant.models import TenantAwareMixin 

# Create your models here.
class Category(TenantAwareMixin):
    code = models.CharField(max_length=20, verbose_name='Category Code')
    description = models.CharField(max_length=50, verbose_name='Category Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Category Detail')

    def __str__(self):
        return self.description

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_category_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_category_description')
        ]
        ordering = ['code']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(TenantAwareMixin):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='Category')
    code = models.CharField(max_length=20, verbose_name='Product Code')
    description = models.CharField(max_length=50, verbose_name='Product Description')
    detail = models.CharField(max_length=100, blank=True, verbose_name='Product Detail')
    photo = models.ImageField(verbose_name='Product Photo')

    def __str__(self):
        return self.description

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tenant','code'], name='unique_product_code'),
            models.UniqueConstraint(fields=['tenant','description'],name='unique_product_description')
        ]
        ordering = ['category','code']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
