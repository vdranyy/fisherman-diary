from django import forms
from django.test import TestCase
from registration.forms import RegistrationForm


class RegistrationFormTestCase(TestCase):
	
	def test_registration_form_have_username_password_fields(self):
		"""
		Test registration form have username and password fields
		"""
		form = RegistrationForm()
		self.assertIn(form['username'], form)
		self.assertIn(form['password1'], form)
		self.assertIn(form['password2'], form)
		
