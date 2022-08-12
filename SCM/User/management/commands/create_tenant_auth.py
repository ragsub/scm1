from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from SCM.MasterData.models import Store
from SCM.signals import add_tenant_authorization
from SCM.Tenant.models import UserToTenant
from SCM.Tenant.utils import tenant_context, no_tenant_context

class Command(BaseCommand):
    help = 'Create the tenant authority for models'

    models = ['Store','Product','Product in Store','Category']

    def handle(self, *args, **options):
        with no_tenant_context():
            user_to_tenants = UserToTenant.objects.all()
        
        for user_tenant in user_to_tenants:
            tenant_group, created = Group.objects.get_or_create(name=str(user_tenant.tenant))
            tenant_group.user_set.add(user_tenant.user)

            ct = ContentType.objects.get_for_model(Store)
            
            with tenant_context(user_tenant.tenant):
                add_tenant_authorization(user_tenant, ct)