from django import template
from app.models import MenuItem
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('app/main.html')
def draw_menu(menu_name):
    root_menu_items = MenuItem.objects.filter(parent__isnull=True)
    menu_items = MenuItem.objects.filter(parent__in=root_menu_items) | root_menu_items
    return {'menu_items': menu_items, 'menu_name': menu_name}