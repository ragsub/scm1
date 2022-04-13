from django import template
from django.core import serializers

register = template.Library()

@register.filter
def get_fields(obj): 
    return obj._meta.get_fields()

@register.simple_tag
def get_verbose_field_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name

@register.simple_tag
def get_list_from_queryset(obj):
    return serializers.serialize('python',obj)
