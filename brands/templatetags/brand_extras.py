from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='firstchar')
@stringfilter
def firstchar(value):
    return value[0]
