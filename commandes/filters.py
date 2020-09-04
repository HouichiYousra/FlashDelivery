from django_filters import rest_framework as filters
from commandes.models import Livraison


class LivraisonFilter(filters.FilterSet):
    dateTime_livraison = filters.DateTimeFilter(label='dateTime_livraison', method="filter_dateTime_livraison")

    class Meta:
        model = Livraison
        fields = ('etat', 'livreur', 'fd_paid', 'fournisseur_paid', 'dateTime_livraison')

        def filter_dateTime_livraison(self, queryset, name, value):
            return queryset.filter(commande__dateTime_livraison=value)