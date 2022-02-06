from django import template

register = template.Library()

@register.filter(name='prod_subtotal')
def prod_subtotal(price, quantity):
    return price * quantity
