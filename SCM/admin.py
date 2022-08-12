from django.contrib import admin

class TenantAwareMixinAdmin(admin.ModelAdmin):
    readonly_fields=('tenant',)