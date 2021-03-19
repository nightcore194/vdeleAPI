from django.urls import path, include
from . import views

urlpatterns = [
    path('authvk', views.login),
    path('logout', views.logout),
    path('stat', views.get_stat),
]