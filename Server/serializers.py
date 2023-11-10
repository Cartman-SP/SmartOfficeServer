from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'firstname',
                  'secondname',
                  'password',
                  'email',
                  'phonenumber',
                  'username',
                  )


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id',
                  'room_number',
                  'state',
                  ]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id',
                  'ip',
                  'type',
                  'room_id',
                  'name'
                  ]
