from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema

from commandes.models import *

@api_view(['GET'])
@schema(None)
def paiementLivreurs(request):
    res = list(Livraison.objects.values('livreur').annotate(Sum('prix')).filter(fd_paid=False))
    return Response(res)

@api_view(['GET'])
@schema(None)
def paiementFournisseurs(request):
    res = list(Livraison.objects.values('commande__fournisseur').annotate(Sum('commande__prix')).filter(fournisseur_paid=False))
    return Response(res)
