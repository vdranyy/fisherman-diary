from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.forms import RegistrationForm


def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			User.objects.create(username=username, password=password)
		return redirect('/registration/register-complete/')
	else:
		form = RegistrationForm()
	context = {'form': form}
	return render(request, 'registration/registration.html', context)
