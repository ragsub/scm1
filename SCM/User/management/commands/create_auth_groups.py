from django.core.management import BaseCommand
from django.db.models import Q
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Create the authorization groups'

    perms = ['Can add ','Can change ','Can delete ','Can view ']
    models = [{'model':'Store','app':'MasterData'},{'model':'Product','app':'MasterData'}]

    def handle(self, *args, **options):
        owner, created = Group.objects.get_or_create(name='Owner')

        for model in self.models:
            for perm in self.perms:
                ct = ContentType.objects.get(app_label=model['app'], model=model['model'])

                permission = Permission.objects.get(Q(name=str(perm)+str(model)) & Q(content_type=ct))
                owner.permissions.add(permission)

        worker, created = Group.objects.get_or_create(name = 'Worker')
        buyer, created = Group.objects.get_or_create(name = 'Buyer')
