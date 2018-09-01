from django import template
import datetime

register = template.Library()

@register.filter(name='fromunix')
def fromunix(value):
    return datetime.datetime.fromtimestamp(int(value)/1000)

@register.simple_tag
def active(request, pattern):
    if pattern == request.path:
        return 'active'
    else:
        return ''