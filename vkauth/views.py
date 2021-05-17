from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .models import vk_user_id, vk_user_token, vk_user_stat, vk_user_login
import json, urllib3, requests
from django.core import serializers
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
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
    return render(request, 'auth_index.html')
#logout
def logout (request):
    auth_logout(request)
    return redirect('/auth')
#stat
@login_required(login_url='/auth')
def get_stat(request):
    #get token & user
    user = request.user.pk
    user_data = UserSocialAuth.objects.get(user=user)
    user_data_parser = user_data.extra_data
    #get group
    vk_stat_get = vk_user_stat()
    vk_user_ids = vk_user_id()
    vk_user_ls = vk_user_login()
    token = vk_user_token()
    vk_user_ls.login = user_data_parser["id"]
    vk_user_ls.save()
    token.login_for = vk_user_login.objects.get(login=user_data_parser["id"])
    token.token = user_data_parser["access_token"]
    vkgroup = requests.get("https://api.vk.com/method/groups.get?id="+str(user_data_parser["id"])+"&filter=admin&access_token="+str(user_data_parser["access_token"])+"&v=5.130")
    vkgroupjs = vkgroup.json()
    vkgroupjs = vkgroupjs["response"]
    vkgroupjsmas = vkgroupjs["items"]
    if request.method == "POST":
        if 'group' in request.POST:
            mas = request.POST['group']
            vk_user_ids.id_user = mas
            vk_user_ids.save()
            #get stats
            vks = requests.get("https://api.vk.com/method/stats.get?group_id="+str(mas)+"&interval=week&intervals_count=1&stats_group=reach&extended=0&access_token="+str(user_data_parser["access_token"])+"&v=5.130")
            vk = vks.json()
            vkjs = vk["response"]
            vkjs = vkjs[0]["reach"]
            vkjs = vkjs["reach"]
            vk_stat_get.id_user_for = vk_user_id.objects.get(id_user=mas)
            vk_stat_get.reach_by_week = vkjs
            token.save()
            vk_stat_get.save()
            return render(request, 'stat.html', {'mas': vkgroupjsmas, 'stat': vkjs, 'user_group': vk_user_ids.id_user})#настроить свявзку
    return render(request, 'stat.html', {'mas': vkgroupjsmas, 'user_group': vk_user_ids.id_user})

def stat_unity(request):
    user = request.user.pk
    #user_stat=vk_user_stat.objects.get(user=user)
    return render(request, 'index.html')