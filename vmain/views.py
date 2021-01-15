from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserData

class vdeleview(APIView):   
    def user(self, request):
        user = User.objects.all()
        userdata = UserData.objects.all()
        return Response({"user": user, "userdata": userdata})

