# custom_filters.py
from django import template

register = template.Library()


@register.filter(name='dict_key')
def dict_key(d, key_name):
    return d.get(key_name, '')
