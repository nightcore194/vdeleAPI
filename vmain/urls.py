from django.urls import path
from .views import vdeleview
app_name = "vmain"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('vmain/', vdeleview.as_view()),
]