from django import template
from rango.models import Category, Page


register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
	return {'cats': Category.objects.all(), 'act_cat': cat}

@register.inclusion_tag('rango/pages.html')
def get_page_list(category=None):
	if category:
		pages = Page.objects.filter(category=category).order_by('-views')
	else:
		pages = None
	return {'pages': pages}