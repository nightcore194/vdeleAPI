# from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, UserData
from .serializers import UserSerializer, UserDataSerializer, vk_user_stat_serializer
from vkauth.models import vk_user_stat

class User(APIView):
    def get(self, request):
        user = User.objects.all()
        userserializer = UserSerializer(user, many=True)
        return Response({"user": userserializer.data})

    def post(self, request):
        user = request.data.get('user')
        userserializer = UserSerializer(data=user)
        if userserializer.is_valid(raise_exception=True):
            user_saved = userserializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.user)})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        user = request.data.get('user')
        user_serializer = UserSerializer(instance=saved_user, data=user, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_saved = user_serializer.save()
        return Response({"success": "User '{}' updated successfully".format(user_saved.user)})

    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=204)

class UserData(APIView):
    def get(self, request):
        userdata = UserData.objects.all()
        userdataserializer = UserDataSerializer(userdata, many=True)
        return Response({"userdata": userdataserializer.data})

    def post(self, request):
        userdata = request.data.get('userdata')
        userdataserializer = UserDataSerializer(data=userdata)
        if userdataserializer.is_valid(raise_exception=True):
            userdata_saved = userdataserializer.save()
        return Response({"success": "UserData '{}' created successfully".format(userdata_saved.userdata)})

    def put(self, request, pk):
        saved_userdata = get_object_or_404(UserData.objects.all(), pk=pk)
        userdata = request.data.get('userdata')
        userdata_serializer = UserSerializer(instance=saved_userdata, data=userdata, partial=True)
        if userdata_serializer.is_valid(raise_exception=True):
            userdata_saved = userdata_serializer.save()
        return Response({"success": "UserData '{}' updated successfully".format(userdata_saved.userdata)})

    def delete(self, request, pk):
        userdata = get_object_or_404(UserData.objects.all(), pk=pk)
        userdata.delete()
        return Response({"message": "UserData with id `{}` has been deleted.".format(pk)}, status=204)


class vk_user_stat(APIView):
    def get(self, request):
        vk_user_stats = vk_user_stat.objects.all()
        vk_user_statserializer = vk_user_stat_serializer(vk_user_stats, many=True)
        return Response({"vk_user_stats": vk_user_statserializer.data})

    def post(self, request):
        vk_user_stats = request.data.get('vk_user_stats')
        vk_user_statserializer = vk_user_stat_serializer(data=vk_user_stats)
        if vk_user_statserializer.is_valid(raise_exception=True):
            vk_user_stats_saved = vk_user_stat_serializer.save()
        return Response({"success": "vk_user_stats '{}' created successfully".format(vk_user_stats_saved.vk_user_stats)})

    def put(self, request, pk):
        saved_userdata = get_object_or_404(vk_user_stat.objects.all(), pk=pk)
        vk_user_stats = request.data.get('vk_user_stats')
        vk_user_statserializer = vk_user_stat_serializer(instance=saved_userdata, data=vk_user_stats, partial=True)
        if vk_user_statserializer.is_valid(raise_exception=True):
            vk_user_stats_saved = vk_user_statserializer.save()
        return Response({"success": "vk_user_stats '{}' updated successfully".format(vk_user_stats_saved.vk_user_stats)})

    def delete(self, request, pk):
        vk_user_stats = get_object_or_404(vk_user_stat.objects.all(), pk=pk)
        vk_user_stats.delete()
        return Response({"message": "vk_user_stats with id `{}` has been deleted.".format(pk)}, status=204)