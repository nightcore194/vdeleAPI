from rest_framework import serializers
from .models import UserData, User
from vkauth.models import vk_user_stat
class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=16)
    user_email = serializers.EmailField(max_length=32)

    def create(self, validated_data): #метод post
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data): #метод put
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)

        instance.save()
        return instance

class UserDataSerializer(serializers.Serializer):
    user_social_vk = serializers.URLField()
    user_social_inst = serializers.URLField()

    def create(self, validated_data): #метод post
        return UserData.objects.create(**validated_data)

    def update(self, instance, validated_data):  # метод put
        instance.user_social_vk = validated_data.get('user_social_vk', instance.user_social_vk)
        instance.user_social_inst = validated_data.get('user_social_inst', instance.user_social_inst)

        instance.save()
        return instance

class vk_user_stat_serializer(serializers.Serializer):
    reach_by_week = serializers.CharField(max_length=16)

    def create(self, validated_data): #метод post
        return vk_user_stat.objects.create(**validated_data)

    def update(self, instance, validated_data): #метод put
        instance.reach_by_week = validated_data.get('reach_by_week', instance.reach_by_week)

        instance.save()
        return instance