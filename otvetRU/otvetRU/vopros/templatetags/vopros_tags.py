from atexit import register
from django import template
from vopros.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Tag.objects.order_by('tag_name')

@register.simple_tag()
def get_quetions():
    return Quetion.objects.all()
