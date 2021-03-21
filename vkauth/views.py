from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .models import vk_user_id, vk_user_token
import json
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import vk_api, os

#login form vk
def login (request):
    if request.user.is_authenticated:
        return redirect('/stat')
    return render(request, 'index.html')
#logout
def logout (request):
    auth_logout(request)
    return redirect('/login')

def get_stat(request):
    vkstat=vk_api.VkApi(login='89223209959', token='e9f3482b8e31e3d8de7bb6344465006e7dd910da17af915efddcf0b50d79e0bc183888e6a857ebd802931')
    vkstat.auth(token_only=True)
    vk=vkstat.get_api()
    vks=vk.stats.get(group_id='141120778', interval='week')
    return render(request, 'stat.html', {'vkstat':vks})