from django.test import TestCase
from django.core.urlresolvers import resolve
from notes.views import home_page
from django.http import HttpRequest


class HomePageTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'<title>Fisherman Diary</title>', response.content)
