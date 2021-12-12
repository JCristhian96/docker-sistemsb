from django import template

register = template.Library()

@register.filter()
# Funcion para dar formato a el precio
def price_format(value):
    return 'S/. {0:.2f}'.format(value)