from django.db.models.signals import post_save
from django.dispatch import receiver

from commandes.models import Commande


@receiver(post_save, sender=Commande)
def nouvelle_commande_notification(sender, **kwargs):
    message = kwargs['instance']
    send_new_message_push_notification(sender_id=message.sender.id,
                                       recipient_id=message.recipient.id,
                                       content=message.content)