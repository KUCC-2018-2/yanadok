from django import template

register = template.Library()

@register.filter
def get_index(sequence, position):
    return sequence[position]