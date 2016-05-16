from django.test import TestCase
from django.core.urlresolvers import resolve
from registration.views import registration, register_complete


class URLsTestCase(TestCase):
	
	def test_registration_url_uses_registration_view(self):
		"""
		Test that registration url resolves to correct view
		"""
		url = resolve('/registration/registration/')
		self.assertEqual(url.func, registration)
	
	def test_register_complete_url_uses_appropriate_view(self):
		"""
		Test that register-complete url uses appropriate
		view function
		"""
		url = resolve('/registration/register-complete/')
		self.assertEqual(url.func, register_complete)

