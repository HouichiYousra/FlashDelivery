from users.models import *

COMMANDE_ETAT_CHOICES = (
    (1, 'Nouvelle'),
    (2, 'validée'),
    (3, 'suppriméée')
)
LIVRAISON_ETAT_CHOICES = (
    (1, 'acceptée'),
    (2, 'en cours'),
    (3, 'en livraison'),
    (4, 'terminée')
)

class Commande(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, verbose_name='fournisseur')
    dateTime_recup = models.DateTimeField(verbose_name="date de récupération")
    dateTime_livraison = models.DateTimeField(verbose_name="date de livraison")
    adresse_livraison = models.TextField(max_length=500, verbose_name='adresse de livraison')
    tel_livraison = models.IntegerField(verbose_name='numéro de téléphone du client')
    description = models.TextField(max_length=500, verbose_name='description')
    prix = models.IntegerField(verbose_name='prix commande')
    etat = models.PositiveSmallIntegerField(choices=COMMANDE_ETAT_CHOICES)

    def __str__(self):
        return self.description

class Livraison(models.Model):
    code = models.TextField(max_length=200, verbose_name='code de validation')
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, verbose_name='commande')
    livreur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='livreur')
    prix = models.IntegerField(verbose_name='prix livraison')
    etat = models.PositiveSmallIntegerField(choices=LIVRAISON_ETAT_CHOICES)
    fd_paid = models.BooleanField(default=False)
    fournisseur_paid = models.BooleanField(default=False)
    feedback = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.commande.description
