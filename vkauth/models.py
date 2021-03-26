from django.db import models
from django.conf import settings
# Create your models here.
class vk_user_login(models.Model): #login юзеров
    login = models.AutoField(primary_key=True)

    def __str__(self):
        return self.login

class vk_user_id(models.Model): #id юзеров
    id_user = models.AutoField(primary_key=True)

    def __str__(self):
        return self.id_user

class vk_user_token(models.Model): #access_token
    token = models.CharField(max_length=1000),
    login = models.OneToOneField(vk_user_login, to_field='login', on_delete=models.CASCADE)

    def __str__(self):
        return self.token

class vk_user_stat(models.Model):#stat юзера
    reach_by_week = models.CharField(max_length=1000),
    id_user = models.OneToOneField(vk_user_id, to_field='id_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.reach_by_week
