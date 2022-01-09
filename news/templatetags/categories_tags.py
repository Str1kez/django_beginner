from django import template

from news.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()

# @register.inclusion_tag('news/dropdown_menu.html')
# def get_dropdown_menu():
#     categories = Category.objects.all()
#     return {'categories': categories}
