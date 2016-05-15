from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput)
	password1 = forms.CharField(label='Password', max_length=10, min_length=6, widget=forms.TextInput)
	password2 = forms.CharField(label='Confirm password', max_length=10, min_length=6, widget=forms.TextInput)
	
	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password didn\'t match')
		return password2
