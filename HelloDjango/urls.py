from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Server.views import *
from Website.views import *

urlpatterns = [
    path("", main_page, name='main_page'),
    path('authenticate/', UserAuthenticationView.as_view(), name='user-authentication'),
    path('qr_scan/<int:qr_id>/', qrscan, name='qr_scan'),
    path('api/rooms', room_view, name="room_view"),
    path('search/', search, name='search'),
]
