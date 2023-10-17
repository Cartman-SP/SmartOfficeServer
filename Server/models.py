from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=15)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=13)


class Passes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(("Date and Time"), auto_now=True)


class Room(models.Model):
    room_number = models.CharField(max_length=20)
    state = models.BooleanField(default=True)


class Device(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
