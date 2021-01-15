# from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, UserData
from .serializers import UserSerializer, UserDataSerializer


class vdeleview(APIView):
    def get(self, request):
        user = User.objects.all()
        userserializer = UserSerializer(user, many=True)
        userdata = UserData.objects.all()
        userdataserializer = UserDataSerializer(userdata, many=True)
        return Response({"user": userserializer.data, "userdata": userdataserializer .data})

    def post(self, request):
        user = request.data.get('user')
        userserializer = UserSerializer(data=user)
        userdata = request.data.get('userdata')
        userdataserializer = UserDataSerializer(data=userdata)
        if userserializer.is_valid(raise_exception=True):
            user_saved = userserializer.save()
        if userdataserializer.is_valid(raise_exception=True):
            userdata_saved = userdataserializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.user), "success": "UserData '{}' created successfully".format(userdata_saved.user)})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        user = request.data.get('user')
        user_serializer = UserSerializer(instance=saved_user, data=user, partial=True)
        saved_userdata = get_object_or_404(UserData.objects.all(), pk=pk)
        userdata = request.data.get('userdata')
        userdata_serializer = UserSerializer(instance=saved_user, data=userdata, partial=True)

        if user_serializer.is_valid(raise_exception=True):
            user_saved = user_serializer.save()

        if userdata_serializer.is_valid(raise_exception=True):
            userdata_saved = userdata_serializer.save()

        return Response({"success": "User '{}' updated successfully".format(user_saved.user), "success": "UserData '{}' updated successfully".format(userdata_saved.user)})

    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        userdata = get_object_or_404(UserData.objects.all(), pk=pk)
        userdata.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, {"message": "UserData with id `{}` has been deleted.".format(pk)}, status=204)