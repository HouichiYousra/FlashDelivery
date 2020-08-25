from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from users import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewset, basename='users')
router.register(r'fournisseurs', views.FournisseurViewset, basename='fournisseurs')


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    url(r'registration/', views.CustomRegisterView.as_view(), name='registration'),
    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    path('', include(router.urls)),

]