from django import template

register = template.Library()

@register.filter(name='search_tags')
def search_tags(value, list):
    tags = set(value.tags)
    for tag in list:
        if tag in tags:
            return True
    return False