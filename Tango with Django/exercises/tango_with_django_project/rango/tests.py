from datetime import datetime, timedelta

from django.test import TestCase
from django.core.urlresolvers import reverse

from rango.models import Category, Page


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """ 
        This should result True for categories where views are zero or positive
        """
        categories = Category.objects.all()
        for c in categories:
            c.delete()
            
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class PageMethodTests(TestCase):

    def test_ensure_visits_are_not_in_future(self):
        """
        The first or last visit should be reset to the current date if the date is set in the future.
        """
        pages = Page.objects.all()
        for c in pages:
            c.delete()
        tomorrow = datetime.today() + timedelta(1)
        today = datetime.today()
        category = Category.objects.get_or_create(name='test')[0]
        page = Page(category=category, title='Django Docs', url='https://docs.djangoproject.com/en/1.8/')
        page.first_visit = tomorrow
        page.last_visit = tomorrow
        page.save()
        self.assertEqual(page.first_visit.date(), today.date())
        self.assertEqual(page.last_visit.date(), today.date())

    def test_ensure_last_vist_is_equal_to_or_after_first_visit(self):
        """
        The first visit is set to the date of the last visit if the last visit comes before first visit.
        """
        pages = Page.objects.all()
        for c in pages:
            c.delete()

        tomorrow = datetime.today() + timedelta(1)
        today = datetime.today()
        category = Category.objects.get_or_create(name='test')[0]
        page = Page(category=category, title='Django Docs', url='https://docs.djangoproject.com/en/1.8/')
        page.first_visit = tomorrow
        page.last_visit = today
        page.save()
        self.assertEqual(page.first_visit <= page.last_visit, True)


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        add_cat('test', 1, 1)
        add_cat('temp', 1, 1)
        add_cat('tmp', 1, 1)
        add_cat('tmp test temp', 1, 1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)
