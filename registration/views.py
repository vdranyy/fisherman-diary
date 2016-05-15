from django.shortcuts import render
from registration.forms import RegistrationForm


def registration(request):
	context = {'form': RegistrationForm()}
	return render(request, 'registration/registration.html', context)
