from django.urls import path

from paiement import views

urlpatterns = [
    path('livreurs/', views.paiementLivreurs, name='livreurs'),
    path('fournisseurs/', views.paiementFournisseurs, name='fournisseurs')
]