from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.login),
    path('logout', views.logout),
    path('stat', views.get_stat),
]