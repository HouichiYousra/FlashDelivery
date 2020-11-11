from django.urls import path

from paiement import views

urlpatterns = [
    path('paieLivreurs/', views.paiementLivreurs, name='paieLivreurs'),
    path('paieFournisseurs/', views.paiementFournisseurs, name='paieFournisseurs')
]