from django import template

register = template.Library()


@register.filter(name='is_filters_uses')
def is_filters_uses(value):
    filters_arg = value.find('&')
    if filters_arg != -1:
        is_first_list_now = value.find('?')
        if value[(is_first_list_now + 1): (is_first_list_now + 5)] == 'page':
            return value[filters_arg:]
        else:
            return ('&' + value[is_first_list_now + 1:])
    else:
        return ''
