from django.urls import path, include
from rest_framework import routers

from commandes import views

router = routers.DefaultRouter()
router.register(r'commandes', views.CommandeViewset, basename='commandes')
router.register(r'livraisons', views.LivraisonViewset, basename='livraisons')
router.register(r'livraisonsLivreur', views.LivraisonLivreurViewset, basename='livraisonsLivreur')


urlpatterns = [
    path('', include(router.urls)),
]