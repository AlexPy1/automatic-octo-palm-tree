from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .utils import random_alphanumeric_string


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        phone_number = kwargs.get("phone_number", None)
        if not phone_number:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = User.objects.get(phone_number=phone_number)
        except:
            return Response({"error": "Object does not exists"})
        if not instance.friend_invite:
            try:
                true_inv = User.objects.get(you_invite_code=request.data['friend_invite'])
                serializer = UserSerializer(data=request.data, instance=instance,
                                            partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except:
                return Response ({"Error": 'Unknown invite code'})
            return Response({"Update_profile": serializer.data})
        else:
            return Response({"Error": 'Invite code is used'})

    def post(self, request):
        try:
            user = User.objects.get(phone_number=request.data['phone_number'])
            return Response(model_to_dict(user))
        except ObjectDoesNotExist:
            user_new = User.objects.create(
                phone_number=request.data['phone_number'],
                you_invite_code=random_alphanumeric_string(6))
            user = User.objects.get(phone_number=request.data['phone_number'])
            return Response(model_to_dict(user))


class GetUserFriendsAPIView(APIView):

    def get(self, request):
        users = User.objects.filter(friend_invite=request.data['friend_invite'])
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
