from django.shortcuts import render, redirect
from vkauth import views

def index(request):
    if request.method == "POST":
        return redirect("/authvk")
    return render(request, 'temp/front/index.html')