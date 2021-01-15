from django.db import models

class User(models.Model): #модель юзера
    user_name = models.CharField(max_length=16)
    user_email = models.EmailField(verbose_name='email address', max_length=32, unique=True,)

    def __str__(self):
        return self.user_name
        return self.user_email

class UserData(models.Model): #модель соц. сети
    user_social_vk = models.URLField(max_length=40)
    user_social_inst = models.URLField(max_length=40)

    def __str__(self):
        return self.user_social_vk
        return self.user_social_inst

# Create your models here.
