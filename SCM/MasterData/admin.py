from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from SCM.MasterData.models import Store
from SCM.admin import TenantAwareMixinAdmin

class StoreAdmin(TenantAwareMixinAdmin, GuardedModelAdmin):
    list_display = ('tenant','code','description','detail')
    list_filter = ('tenant','code','description','detail')

admin.site.register(Store, StoreAdmin)
