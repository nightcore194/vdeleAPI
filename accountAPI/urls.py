from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^main/', views.main, name='main'),
    url(r'^main/login', views.login, name='login'),
    url(r'^account/', views.edit, name='account'),
    url(r'^main/registration', views.registration, name='registration'),
    url(r'^main/login/forgotpass/$', 'django.contrib.auth.views.forgotpass', name='forgotpass'),
    url(r'^main/login/forgotpass/done/$', 'django.contrib.auth.views.forgotpass_done', name='forgotpass_done'),
    url(r'^main/login/forgotpass/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.forgotpass_confirm', name='forgotpass_confirm'),
    url(r'^main/login/forgotpass/complete/$', 'django.contrib.auth.views.forgotpass_complete', name='forgotpass_complete'),
    url(r'^account/edit/$', views.edit, name='edit'),
]
