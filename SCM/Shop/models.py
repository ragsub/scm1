from django.contrib.auth import get_user_model
from django.db import models

from SCM.Tenant.models import TenantAwareMixin
from SCM.MasterData.models import Store
from SCM.Product.models import Product

class Cart(TenantAwareMixin):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    store = models.ForeignKey(to=Store,on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super(Cart, self).save(*args, **kwargs)
