from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from registration.views import registration
from registration.forms import RegistrationForm


class ViewsTestCase(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_registration_view_basic(self):
		"""
		Test that registration view returns a 200 response and uses corect
		template
		"""
		request = self.factory.get('/registration/registration/')
		with self.assertTemplateUsed('registration/registration.html'):
			response = registration(request)
			self.assertEqual(response.status_code, 200)

	def test_registration_view_returns_registration_form(self):	
		"""
		Test that registration view returns html form
		"""
		response = self.client.get('/registration/registration/')
		self.assertIs(type(response.context['form']), RegistrationForm)
	
