# lottery/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def range_filter(value, arg):
    return range(value, arg)

@register.filter
def subtract(value, arg):
    return value - arg