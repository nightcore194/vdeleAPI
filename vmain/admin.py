from django.contrib import admin
from .models import UserData, User
# Register your models here.
admin.site.register(User)
admin.site.register(UserData)
