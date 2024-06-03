from django import template
from foodwaste.models import *
register = template.Library()

@register.filter(name = 'notification')
def notification(obj):
    foodrequest  = Foodrequests.objects.filter(status=None)
    return foodrequest

@register.simple_tag()
def notificationcount(*args, **kwargs):
    foodrequestcount  = Foodrequests.objects.filter(status=None).count()
    return foodrequestcount