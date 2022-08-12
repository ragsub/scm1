from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,default="")
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS

    objects = UserManager()


class Authority(models.Model):
    permission = None
    tenant = None
    user = None
    group = None
    type = None
    owner_group=None
    worker_group=None
    shipper_group=None

    def __init__(self, tenant=None, user=None, type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tenant = tenant
        self.user = user
        self.type = type

        self.add_tenant_permission()
        self.add_tenant_group()
        self.assign_tenant_permission_to_group()
        self.assign_user_to_group()

        if self.type == None:
            return

        if self.type == 'Owner':
            self.add_owner_group()

    class Meta:
        managed = False  
        default_permissions = ()

    def add_tenant_group(self):
        self.group, created = Group.objects.get_or_create(name=self.tenant.tenant)
    
    def add_tenant_permission(self):
        content_type = ContentType.objects.get(model=self.__class__)
        self.permission = Permission.objects.create(
            codename=self.tenant.tenant, 
            name='Can access ' + self.tenant.tenant,
            content_type=content_type)

    def assign_tenant_permission_to_group(self):
        self.group.permissions.add(self.permission)

    def assign_user_to_group(self):
        self.group.user_set.add(self.user)

    def add_owner_group(self):
        tenant_owner = self.tenant.tenant + "_owner"
        self.owner_group, created = Group.objects.get_or_create(name=tenant_owner)

    def add_owner_permissions(self):
        perms = ['Can add ','Can change ','Can delete ','Can view ']
        models = ['Store','Product','Product in Store','Category']

        for model in self.models:
            for perm in self.perms:
                permission = Permission.objects.get(name=str(perm)+str(model))
                self.owner_group.permissions.add(permission)


