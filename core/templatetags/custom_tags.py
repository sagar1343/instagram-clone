from django import template

register = template.Library()


@register.filter
def short_time(date):
    return date.split(",")[0]
