from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.annotate(article_count=Count('article')).filter(article_count__gt=0)

# @register.inclusion_tag('news/dropdown_menu.html')
# def get_dropdown_menu():
#     categories = Category.objects.all()
#     return {'categories': categories}
