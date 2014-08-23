from django import template

register = template.Library()

@register.filter(name='dictkeyvalue')
def dictkeyvalue(dict, key):    
    return dict[key] 
