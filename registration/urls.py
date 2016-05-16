from django.conf.urls import  url

urlpatterns = [
    url(r'registration/$', 'registration.views.registration', name='registration'),
	url(r'register-complete/$', 'registration.views.register_complete', name='register_complete'),
]
