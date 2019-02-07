from django import template

import os

register = template.Library()

@register.filter(name='get_filename')
def get_filename(value):
    return os.path.basename(value.file.name)
