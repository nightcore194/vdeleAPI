from django.db import models
from django.conf import settings
# Create your models here.
class vk_user_id(models.Model): #id юзеров
    login = models.CharField(max_length=30)

    def __str__(self):
        return self.login

class vk_user_token(models.Model): #access_token
    token = models.CharField(max_length=1000)
    login = models.ForeignKey('vk_user_id', on_delete=models.CASCADE,)

    def __str__(self):
        return self.token

