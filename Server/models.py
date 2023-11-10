from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=15)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=13)
    groups = models.ManyToManyField('auth.Group', related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users')



class Passes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time = models.DateTimeField(("Date and Time"), auto_now=True)


class Room(models.Model):
    room_number = models.CharField(max_length=20)
    state = models.BooleanField(default=True)


class Device(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
