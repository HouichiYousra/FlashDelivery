from rest_framework import serializers
from .models import *



class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class CommandeFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('fournisseur', 'dateTime_recup', 'dateTime_livraison', 'adresse_livraison', 'tel_livraison',
                  'description', 'prix')
class CommandeModerateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('etat',)


class LivraisonSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer(many=False, read_only=True)
    class Meta:
        model = Livraison
        fields = '__all__'

class LivraisonLivreurSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer(many=False, read_only=True)
    class Meta:
        model = Livraison
        exclude = ('fd_paid', 'fournisseur_paid', 'feedback', 'prix', 'code')

class LivraisonLivreurSerializer2(serializers.ModelSerializer):
    commande = CommandeSerializer(many=False, read_only=True)
    class Meta:
        model = Livraison
        exclude = ('code',)

class LivraisonFournisseurSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer(many=False, read_only=True)
    class Meta:
        model = Livraison
        fields = ('feedback',)
