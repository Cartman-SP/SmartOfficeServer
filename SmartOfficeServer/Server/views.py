from rest_framework import viewsets
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import *


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username1 = request.data.get('Username')
        password1 = request.data.get('Password')
        user = User.objects.get(username=username1, password=password1)
        print(user.firstname)
        if user:
            return Response({"status": "success", "email": user.email, "firstname": user.firstname})
        else:
            return Response({"status": "error", "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"status": "error", "message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)


def qrscan(request, qr_id):
    user1 = User.objects.get(id=qr_id)
    pas = Passes.objects.create(user=user1)
    pas.save
    return JsonResponse({'status': 'success'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def room_view(request):
    if request.method == 'POST':
        arr = []
        rooms = Room.objects.all()
        for i in rooms:
            devices = Device.objects.filter(room_id=i)
            arr.append([i.room_number, list(devices.values())])
        print(arr)
        return Response({"status": "success", 'room_number': arr, })
