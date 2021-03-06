from django import template
from django.core import serializers
from SCM.Tenant.models import Tenant

register = template.Library()

@register.simple_tag
def get_tenant_name(tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    return tenant.tenant

@register.simple_tag
def get_plural_verbose_model_name(obj): 
    return obj._meta.verbose_name_plural

@register.simple_tag
def get_verbose_model_name(obj): 
    return obj._meta.verbose_name

@register.simple_tag
def get_verbose_model_name_from_form(obj): 
    return obj._meta.model._meta.verbose_name

@register.simple_tag
def get_verbose_field_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name

@register.simple_tag
def get_list_from_queryset(obj):
    return serializers.serialize('python',obj)

@register.simple_tag
def get_field_value_from_instance(obj):
    return obj.__dict__ 

@register.simple_tag
def get_model_from_page_obj(obj):
    return obj.object_list.model

@register.simple_tag
def url_transform(request, **kwargs):
    """usages: {% url_transform request page=1 %}"""
    updated = request.GET.copy()

    for k, v in kwargs.items():
        updated[k] = v

    return updated.urlencode()

@register.simple_tag
def get_attribute(obj, attribute):
    return getattr(obj,attribute)
