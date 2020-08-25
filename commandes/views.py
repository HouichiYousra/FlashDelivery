from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import *
from .models import *
from .policy import *

class CommandeViewset(viewsets.ModelViewSet):
    permission_classes = (CommandePolicy,)
    serializer_class = CommandeSerializer
    queryset = Commande.objects.all()
    filterset_fields = ['etat', 'dateTime_recup', 'dateTime_livraison', 'fournisseur']

    @action(methods=['PATCH'], detail=True, name='modifier_fournisseur')
    def update_fournisseur(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = CommandeFournisseurSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    @action(methods=['PATCH'], detail=True, name='modifier_moderateur')
    def update_moderateur(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = CommandeModerateurSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_destroy(self, instance):
        if instance.etat == 1:
            instance.delete()
        else:
            pass


class LivraisonFilter(filters.FilterSet):
    dateTime_livraison = filters.DateTimeFilter(label='dateTime_livraison', method="filter_dateTime_livraison")

    class Meta:
        model = Livraison
        fields = ('etat', 'livreur', 'fd_paid', 'fournisseur_paid', 'dateTime_livraison')

        def filter_dateTime_livraison(self, queryset, name, value):
            return queryset.filter(commande__dateTime_livraison=value)


class LivraisonViewset(viewsets.ModelViewSet):
    permission_classes = (LivraisonPolicy,)
    serializer_class = LivraisonSerializer
    queryset = Livraison.objects.all()
    filter_class = LivraisonFilter

    @action(methods=['PATCH'], detail=True, name='modifier_livreur')
    def update_livreur(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = LivraisonLivreurSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    @action(methods=['PATCH'], detail=True, name='ajouter_feedback')
    def ajouter_feedback(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = LivraisonFournisseurSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

class LivraisonLivreurViewset(viewsets.ViewSet):
    serializer_class = LivraisonSerializer
    filter_class = LivraisonFilter

    def list(self, request):
        queryset = Livraison.objects.filter(livreur_id=request.user.id).order_by('commande__dateTime_livraison')
        serializer = LivraisonLivreurSerializer2(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        livraison = get_object_or_404(queryset, pk=pk)
        serializer = LivraisonLivreurSerializer2(livraison)
        return Response(serializer.data)