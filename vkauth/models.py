from django.db import models
from django.conf import settings
# Create your models here.
class vk_user_login(models.Model): #login юзеров
    login = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.login)

class vk_user_id(models.Model): #id юзеров
    id_user = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id_user)

class vk_user_token(models.Model): #access_token
    token = models.CharField(max_length=1000, default=0)
    login_for = models.OneToOneField(vk_user_login, to_field='login', on_delete=models.CASCADE, default=0)


    def __str__(self):
        return str(self.token)

class vk_user_stat(models.Model):#stat юзера
    reach_by_week = models.CharField(max_length=1000, default=0)
    id_user_for = models.OneToOneField(vk_user_id, to_field='id_user', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.reach_by_week)
