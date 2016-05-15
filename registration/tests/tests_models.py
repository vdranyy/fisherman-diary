from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTestCase(TestCase):
	
	def test_saving_and_retreaving_users(self):
		"""
		Test can save and retreave user objects
		"""
		user = User.objects.create(
			username='fisherman-bob',
			password='BoBfish23'
		)
		saved_user = User.objects.get(username='fisherman-bob')
		self.assertEqual(saved_user.username, 'fisherman-bob')

