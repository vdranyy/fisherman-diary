from django.conf.urls import  url

urlpatterns = [
    url(r'registration/$', 'registration.views.registration', name='registration'),
]
