from django.db.models.signals import post_save

from commandes.models import *
from fcm_django.models import FCMDevice

@receiver(post_save, sender=Commande)
def nouvelle_commande_notification(sender, **kwargs):
    device = FCMDevice.objects.all().first() # send to all moderateurs
    device.send_message(title='Nouvelle commande', body='') # body?


@receiver(post_save, sender=Livraison)
def nouvelle_livraison_notification(sender, **kwargs):
    device = FCMDevice.objects.all().first()  # send to le livreur
    device.send_message(title='Nouvelle livraison', body='')  # body?

# notifier le fournisseur du changement d'état d'une livraison
# notifier l'admin si une commande n'est pas terminée après la date de livraison