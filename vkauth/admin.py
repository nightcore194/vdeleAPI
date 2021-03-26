from django.contrib import admin
from .models import vk_user_stat, vk_user_id, vk_user_token, vk_user_login
admin.site.register(vk_user_token)
admin.site.register(vk_user_id)
admin.site.register(vk_user_stat)
admin.site.register(vk_user_login)
# Register your models here.
