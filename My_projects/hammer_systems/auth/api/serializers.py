from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", 'you_invite_code', 'friend_invite')

    def update(self, instance, validated_data):
        instance.friend_invite = validated_data.get("friend_invite", instance.friend_invite)
        instance.save()
        return instance
