from django import template
from django.core import serializers

register = template.Library()

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
def url_transform(request, **kwargs):
    """usages: {% url_transform request page=1 %}"""
    updated = request.GET.copy()

    for k, v in kwargs.items():
        updated[k] = v

    return updated.urlencode()
