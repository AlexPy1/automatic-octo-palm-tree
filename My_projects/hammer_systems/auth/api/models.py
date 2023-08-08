from django.db import models


class User(models.Model):
    phone_number = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    you_invite_code = models.CharField(max_length=255)
    friend_invite = models.CharField(max_length=255)



