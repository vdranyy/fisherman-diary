from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from registration.views import registration, register_complete
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
	
	def test_registration_view_can_save_post_request(self):	
		"""
		Test that registration view can save a POST request
		"""
		request = HttpRequest()
		request.method = 'POST'
		request.POST['user'] = User.objects.create_user(username='fisherman-bob', password='BoBfish23')
		response = registration(request)
		
		self.assertEqual(User.objects.count(), 1)
		user = User.objects.first()
		self.assertEqual(user.username, 'fisherman-bob')
		self.assertEqual(response.status_code, 200)

	def test_registration_view_saves_user_only_if_user_is_valid(self):
		"""
		Test that user can be save only if user data is valid
		"""
		request = HttpRequest()
		registration(request)
		self.assertEqual(User.objects.count(), 0)


	#def test_registration_view_redirects_after_saving_user(self):
		"""
		Test that registration view redirects to confirmation
		page after saving user
		"""
		#request = HttpRequest()
		#response = registration(request)

	def test_register_complete_view_basic(self):
		"""
		Test that register_complete view returns a 200 responce
		and uses correct template
		"""
		request = self.factory.get('/registration/register-complete/')
		with self.assertTemplateUsed('registration/register_complete.html'):
			response = register_complete(request)
			self.assertEqual(response.status_code, 200)

