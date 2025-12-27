from django import template

register = template.Library()

@register.filter
def split_tags(value):
    if value:
        return [tag.strip() for tag in value.split(',') if tag.strip()]
    return []
