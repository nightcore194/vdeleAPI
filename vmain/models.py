from django.db import models

class User(models.Model): #модель юзера
    user_name = models.CharField(max_length=16)
    user_email = models.EmailField(verbose_name='email address', max_length=32, unique=True,)

    def __str__(self):
        return self.user_name

class UserData(models.Model): #модель соц. сети
    user_social_vk = models.URLField()
    user_social_inst = models.URLField()
    user = models.ForeignKey('User', on_delete=models.CASCADE,)

    def __str__(self):
        return self.user_social_vk


