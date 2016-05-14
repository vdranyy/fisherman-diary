from django.test import TestCase
from django.core.urlresolvers import resolve
from registration.views import registration


class URLsTestCase(TestCase):
	
	def test_registration_url_uses_registration_view(self):
		urls = resolve('/registration/registration/')
		self.assertEqual(urls.func, registration)
