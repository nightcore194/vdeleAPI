from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .models import vk_user_id, vk_user_token, vk_user_stat
import json
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import vk_api
#main page view
def index(request):
    if request.user.is_authenticated:
        return redirect('/stat')
    else:
        if request.method == "POST":
            return redirect('/auth')
    return render(request, 'main.html', {'user': request.user})
#login form vk
def login (request):
    if request.user.is_authenticated:
        return redirect('/stat')
    return render(request, 'index.html')
#logout
def logout (request):
    auth_logout(request)
    return redirect('/auth')
#stat
@login_required(login_url='/auth')
def get_stat(request):
    vk_stat = vk_api.VkApi(login='89223209959', token='e9f3482b8e31e3d8de7bb6344465006e7dd910da17af915efddcf0b50d79e0bc183888e6a857ebd802931')
    vk_stat.auth(token_only=True)
    vk = vk_stat.get_api()
    vk_stat_get = vk_user_stat()
    vkgroup = vk.groups.get(id='194890660', filter='admin')
    vkgroup = json.dumps(vkgroup[0]['items'])
    vkgroup = json.loads(vkgroup)
    vks = vk.stats.get(group_id=vkgroup['id'], interval='week', intervals_count=1, stats_group='reach', extended=0)
    vks = json.dumps(vks[0]["reach"])
    vks = json.loads(vks)
    vk_stat_get.reach_by_week = vks["reach"]
    vk_stat_get.save()
    return render(request, 'stat.html')