from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.forms import RegistrationForm


def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.clean_password()
			User.objects.create_user(username=username, password=password)
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/registration/register-complete/')
	else:
		form = RegistrationForm()
	context = {'form': form}
	return render(request, 'registration/registration.html', context)


def register_complete(request):
	return render(request, 'registration/register_complete.html')
