from django.urls import path
from .views import vk_user_stat, User, UserData
app_name = "vmain"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', User.as_view()),
    path('user/<int:pk>', User.as_view()),
    path('userdata/', UserData.as_view()),
    path('userdata/<int:pk>', UserData.as_view()),
    path('vk_user_stat/', vk_user_stat.as_view()),
    path('vk_user_stat/<int:pk>', vk_user_stat.as_view()),
]