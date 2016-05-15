from django.test import TestCase
from django.core.urlresolvers import resolve
from registration.views import registration


class URLsTestCase(TestCase):
	
	def test_registration_url_uses_registration_view(self):
		"""
		Test that registration url resolves to correct view
		"""
		urls = resolve('/registration/registration/')
		self.assertEqual(urls.func, registration)
