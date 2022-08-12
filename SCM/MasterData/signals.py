from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from SCM.signals import add_tenant_authorization
from SCM.Tenant.models import UserToTenant
from SCM.MasterData.models import Store

@receiver(post_save, sender=UserToTenant)
def add_tenant_authorization_to_store(instance, **kwargs):
    ct = ContentType.objects.get_for_model(Store)
    add_tenant_authorization(instance, ct)


    
