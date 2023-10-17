from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Server.views import UserViewSet
from Server.views import *
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/authenticate', login_view, name='login_view'),
    path('qr_scan/<int:qr_id>/', qrscan, name='qr_scan'),
    path('api/rooms', room_view, name="room_view"),
]
