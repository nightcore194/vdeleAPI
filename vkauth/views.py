from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .models import vk_user_id, vk_user_token, vk_user_stat, vk_user_login
import json
from django.core import serializers
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
    #get token & user
    user_data = UserSocialAuth()
    user_data_parser = serializers.serialize("json", user_data.extra_data)
    user_data_parser = json.dumps(user_data_parser)
    #user
    user_login = vk_user_login()
    user_login.login = json.loads(user_data_parser["email"])
    user_login.save()
    #token
    user_token = vk_user_token()
    user_token.login = user_login.login
    user_token.token = json.loads(user_data_parser["access_token"])
    user_token.save()
    #auth login
    vk_stat = vk_api.VkApi(login=user_token.login, token=user_token.token)
    vk_stat.auth(token_only=True)
    vk = vk_stat.get_api()
    #get group
    vk_stat_get = vk_user_stat()
    vk_user_ids = vk_user_id()
    user_id = json.loads(user_data_parser["id"])
    vk_user_ids.id_user = user_id
    vkgroup = vk.groups.get(id=user_id, filter='admin')
    vkgroup = json.dumps(vkgroup["items"])
    vkgroup = json.loads(vkgroup)
    #get stats
    vks = vk.stats.get(group_id=vkgroup[0], interval='week', intervals_count=1, stats_group='reach', extended=0)
    vks = json.dumps(vks[0]["reach"])
    vks = json.loads(vks)
    vk_stat_get.id_user = user_id
    vk_stat_get.reach_by_week = vks["reach"]
    vk_stat_get.save()
    return render(request, 'stat.html')