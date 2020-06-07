from django import template

register = template.Library()

@register.filter(name='search_filter')
def search_filter(value, list):
    tlist = value.tags[1:-1]
    tags = set(list(tlist))
    for tag in list:
        if tag in tags:
            return True
    return False