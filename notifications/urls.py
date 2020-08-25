from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]