from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Server.views import *
from Website.views import *
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("start/", main_page, name='main_page'),
    path('api/authenticate', login_view, name='login_view'),
    path('qr_scan/<int:qr_id>/', qrscan, name='qr_scan'),
    path('api/rooms', room_view, name="room_view"),
    path('search/', search, name='search'),
]
