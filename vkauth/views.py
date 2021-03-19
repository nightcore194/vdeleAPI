from django.shortcuts import render, redirect
from social_django.models import AbstractUserSocialAuth
from .models import vk_user_id, vk_user_token
import json
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import vk_api, os

#login form vk
def login (request):
    if request.method == "POST":
        deser = json.loads(AbstractUserSocialAuth.extra_data()) #десериализация
        vk_id = vk_user_id()
        vk_id.login = deser['id']
        vk_token = vk_user_token
        vk_token.token = deser['access_token']
        vk_id.save()
        vk_token.save()
        return redirect("get_stat")
    return render(request, 'index.html')

def logout (request):
    auth_logout(request)
    return redirect('/')

def get_stat(request):
    return render(request, 'stat.html')