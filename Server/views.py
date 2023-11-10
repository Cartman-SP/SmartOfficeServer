from rest_framework import viewsets
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
import sys
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import CustomUser

class UserAuthenticationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Проведите проверку аутентификации
        user = authenticate(username=username, password=password)

        if user is not None:
            # Аутентификация успешна
            token, _ = Token.objects.get_or_create(user=user)
            serializer = CustomUserSerializer(user)
            return Response({'user': serializer.data, 'token': token.key})
        else:
            # Аутентификация неуспешна
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
